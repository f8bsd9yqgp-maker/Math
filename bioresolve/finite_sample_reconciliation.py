"""BioResolve v1.9: honest-input fault-tolerant Poisson interval reconciliation.

This is a rigorous *conditional* mathematical solution, not a novel statistical
method or proof of empirical instrument calibration. It provides finite-sample
coverage under explicitly bounded instrument gains, independent of how faulty
instruments behave. The sources of each bound must be separately validated.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import inf, isfinite
from collections import defaultdict
from scipy.stats import chi2


@dataclass(frozen=True)
class CountMeasurement:
    """count ~ Poisson(exposure * gain * theta), gain in [gain_min,gain_max]."""
    count: int
    exposure: float
    gain_min: float
    gain_max: float

    def validate(self) -> None:
        if isinstance(self.count, bool) or not isinstance(self.count, int) or self.count < 0:
            raise ValueError('Count must be a nonnegative integer')
        if not (isfinite(self.exposure) and self.exposure > 0 and
                isfinite(self.gain_min) and isfinite(self.gain_max) and
                0 < self.gain_min <= self.gain_max):
            raise ValueError('Exposure and gain bounds must be finite and positive')


def poisson_mean_interval(k: int, error_probability: float) -> tuple[float,float]:
    """Garwood equal-tail confidence interval for Poisson mean, including k=0.

    The coverage is >= 1-error_probability for each true Poisson mean.
    """
    if isinstance(k, bool) or not isinstance(k,int) or k < 0 or not 0 < error_probability < 1:
        raise ValueError('Invalid count or probability')
    lo = 0. if k == 0 else float(chi2.ppf(error_probability/2,2*k)/2)
    hi = float(chi2.ppf(1-error_probability/2,2*(k+1))/2)
    return lo, hi


def measurement_theta_interval(m: CountMeasurement, alpha: float) -> tuple[float,float]:
    """Conservative theta CI with bounded multiplicative calibration gain."""
    m.validate()
    lo,hi=poisson_mean_interval(m.count, alpha)
    return lo/(m.exposure*m.gain_max),hi/(m.exposure*m.gain_min)


def intersection_of_at_least_k_closed_intervals(intervals: list[tuple[float,float]], k: int) -> list[tuple[float,float]]:
    """Exact union of all real x covered by >= k of the CLOSED intervals.

    Runs O(n log n), and preserves single-point overlap and disconnected
    components. No use of sensor independence. Output sorted, merged components.
    """
    n=len(intervals)
    if not 1 <= k <= n:
        raise ValueError('Require 1 <= k <= number of intervals')
    events=defaultdict(lambda:[0,0])
    for lo,hi in intervals:
        if not (lo <= hi):
            raise ValueError('Invalid interval')
        events[lo][0]+=1
        events[hi][1]+=1
    xs=sorted(events)
    segments=[]
    coverage_open_before=0
    for i,x in enumerate(xs):
        starts,ends=events[x]
        point_count=coverage_open_before+starts
        after_count=point_count-ends
        if point_count>=k:
            segments.append((x,x))
        if i+1<len(xs) and after_count>=k and x < xs[i+1]:
            segments.append((x,xs[i+1]))
        coverage_open_before=after_count
    if coverage_open_before != 0:
        raise AssertionError('Unbalanced sweep events')
    merged=[]
    for lo,hi in segments:
        if merged and lo<=merged[-1][1]:
            merged[-1]=(merged[-1][0],max(merged[-1][1],hi))
        else:
            merged.append((lo,hi))
    return merged


def reconcile(measurements: list[CountMeasurement], max_faults: int, *, error_probability: float=.05) -> dict:
    """Exact finite-sample fault-tolerant confidence set for theta >= 0.

    Assumption: at least n-max_faults sources have Poisson counts with
    multiplicative gains inside independent, externally justified bounds.
    Conservative >= 1-error_probability coverage follows from Garwood
    marginal coverage plus union bound; counts NEED NOT be independent.
    Others may be arbitrary/adversarial.
    """
    n=len(measurements)
    if n<1 or isinstance(max_faults,bool) or not isinstance(max_faults,int) or not 0<=max_faults<n:
        raise ValueError('Need >= 1 source and max_faults from 0 through n-1')
    if not 0<error_probability<1:
        raise ValueError('Invalid global error probability')
    alpha=error_probability/n
    intervals=[measurement_theta_interval(m,alpha) for m in measurements]
    confidence=intersection_of_at_least_k_closed_intervals(intervals,n-max_faults)
    return {'intervals':intervals,'feasible_set':confidence,'n':n,
            'minimum_honest':n-max_faults,'individual_error_budget':alpha,
            'guaranteed_coverage_if_assumptions_hold':1-error_probability,
            'status':'CONSISTENT' if confidence else 'MODEL_OR_CALIBRATION_CONFLICT'}


def contains(components: list[tuple[float,float]], theta: float) -> bool:
    return any(lo<=theta<=hi for lo,hi in components)


@dataclass(frozen=True)
class RatioMeasurement:
    """A and B counts from Poisson rates with relative assay efficiency bounds.

    count_a ~ Poi(depth_a * eff_a * concentration_a)
    count_b ~ Poi(depth_b * eff_b * concentration_b)
    efficiency_b_over_a in [eff_ratio_min,eff_ratio_max]
    """
    count_a: int
    count_b: int
    depth_a: float
    depth_b: float
    eff_ratio_min: float
    eff_ratio_max: float

    def validate(self) -> None:
        for val in (self.count_a,self.count_b):
            if isinstance(val,bool) or not isinstance(val,int) or val<0:
                raise ValueError('Counts must be nonnegative integers')
        if not (all(isfinite(z) and z>0 for z in
                    (self.depth_a,self.depth_b,self.eff_ratio_min,self.eff_ratio_max))
                and self.eff_ratio_min<=self.eff_ratio_max):
            raise ValueError('Depths and efficiency ratio bounds invalid')


def poisson_ratio_interval(m: RatioMeasurement, error_probability: float) -> tuple[float,float]:
    """Exact conditional Clopper-Pearson confidence interval for theta_A/theta_B.

    Assumes independent Poisson A and B counts, fixed sequencing depths,
    and *externally justified* bounds on per-assay relative efficiencies.
    Conditional on total counts, count_a ~ Binomial(total, p).
    The result is honest for zero reads in one or both groups; both zero
    yields [0, infinity], not a made-up value of ratio 1.
    """
    from scipy.stats import beta
    m.validate()
    if not 0<error_probability<1:raise ValueError('Invalid confidence level')
    a,b=m.count_a,m.count_b
    if a+b==0:return 0.,inf
    lo_p=0. if a==0 else float(beta.ppf(error_probability/2,a,b+1))
    hi_p=1. if b==0 else float(beta.ppf(1-error_probability/2,a+1,b))
    lo=lo_p/(1-lo_p)*m.depth_b/m.depth_a*m.eff_ratio_min
    hi=inf if hi_p==1 else hi_p/(1-hi_p)*m.depth_b/m.depth_a*m.eff_ratio_max
    return lo,hi


def reconcile_ratios(measurements: list[RatioMeasurement], max_faults: int,
                     *, error_probability: float=.05) -> dict:
    """The same O(n log n) complete-set solution for calibrated A/B ratios.

    Assumptions include independent Poisson counts within each valid
    instrument and calibrated between-condition assay efficiency ratios.
    Between-instrument independence is NOT needed for the union-bound proof.
    """
    n=len(measurements)
    if not 0<=max_faults<n or n==0 or not 0<error_probability<1:
        raise ValueError('Invalid fault budget or probability')
    ci=[poisson_ratio_interval(m,error_probability/n) for m in measurements]
    return {'feasible_set':intersection_of_at_least_k_closed_intervals(ci,n-max_faults),
            'instrument_intervals':ci,'nominal_joint_coverage':1-error_probability,
            'min_honest':n-max_faults,
            'status':'CONSISTENT' if intersection_of_at_least_k_closed_intervals(ci,n-max_faults)
            else 'MODEL_OR_CALIBRATION_CONFLICT'}
