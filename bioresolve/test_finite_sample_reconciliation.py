import math, random, unittest
from itertools import combinations
from scipy.stats import poisson
from finite_sample_reconciliation import (
    CountMeasurement, poisson_mean_interval, measurement_theta_interval,
    intersection_of_at_least_k_closed_intervals, reconcile, contains
)

class ReconciliationTests(unittest.TestCase):
    def test_zero_count_poisson_bound(self):
        lo,hi=poisson_mean_interval(0,.05)
        self.assertEqual(lo,0)
        self.assertAlmostEqual(hi,-math.log(.025),places=10)
    def test_malformed(self):
        for k in (-1,True,3.1):
            with self.assertRaises(ValueError):poisson_mean_interval(k,.05)
        with self.assertRaises(ValueError):reconcile([],0)
        with self.assertRaises(ValueError):reconcile([CountMeasurement(0,1,1,2)],1)
        with self.assertRaises(ValueError):measurement_theta_interval(CountMeasurement(0,1,2,1),.05)
    def test_gain_endpoint(self):
        m=CountMeasurement(3,10,.5,2.0)
        lo,hi=poisson_mean_interval(3,.01)
        self.assertEqual(measurement_theta_interval(m,.01),(lo/20,hi/5))
    def test_singleton_overlap(self):
        z=intersection_of_at_least_k_closed_intervals([(0,1),(1,2)],2)
        self.assertEqual(z,[(1,1)])
    def test_disconnected_set(self):
        z=intersection_of_at_least_k_closed_intervals([(0,2),(1,3),(5,7),(6,8)],2)
        self.assertEqual(z,[(1,2),(6,7)])
    def test_empty_set(self):
        z=intersection_of_at_least_k_closed_intervals([(0,1),(2,3)],2)
        self.assertEqual(z,[])
    def test_exact_sweep_against_bruteforce(self):
        rng=random.Random(1709)
        for _ in range(4000):
            n=rng.randint(1,9)
            coords=sorted([rng.randrange(-7,8) for _ in range(2*n)])
            intervals=[(coords[2*i],coords[2*i+1]) for i in range(n)]
            k=rng.randint(1,n)
            answer=intersection_of_at_least_k_closed_intervals(intervals,k)
            # Check every interval endpoint and open-cell representative:
            unique=sorted(set(coords))
            probes=unique+[(a+b)/2 for a,b in zip(unique,unique[1:])]+[unique[0]-1,unique[-1]+1]
            for p in probes:
                brute=sum(a<=p<=b for a,b in intervals)>=k
                self.assertEqual(contains(answer,p),brute,(intervals,k,p,answer))
    def test_garwood_numerical_coverage(self):
        # Finite computation of actual Poisson coverage over support 0...n,
        # for multiple lambda and alpha, using exact Poisson probabilities.
        for alpha in (.05,.01):
            for lam in (.01,.1,.5,1.,2.,5.,20.,80.):
                upper=int(poisson.ppf(1-1e-11,lam))+2
                covered=sum(poisson.pmf(k,lam) for k in range(upper+1)
                    if contains([poisson_mean_interval(k,alpha)],lam))
                self.assertGreaterEqual(covered+1e-10,1-alpha)
    def test_robust_to_fault(self):
        # An adversarial count cannot invalidate coverage when enough honest
        # intervals contain the truth (deterministic event-by-event property).
        m=[CountMeasurement(100,50,1,1),CountMeasurement(103,50,1,1),
           CountMeasurement(0,50,1,1)]
        q=reconcile(m,1)
        self.assertTrue(contains(q['feasible_set'],2.0))
    def test_finite_sample_wide_calibration(self):
        narrow=reconcile([CountMeasurement(40,20,1,1)],0)
        wide=reconcile([CountMeasurement(40,20,.8,1.25)],0)
        self.assertLessEqual(wide['feasible_set'][0][0],narrow['feasible_set'][0][0])
        self.assertGreaterEqual(wide['feasible_set'][0][1],narrow['feasible_set'][0][1])
    def test_strict_boundary_point(self):
        self.assertEqual(intersection_of_at_least_k_closed_intervals([(0,1),(1,2),(1,1)],3),[(1,1)])

if __name__=='__main__':unittest.main()

from finite_sample_reconciliation import RatioMeasurement, poisson_ratio_interval,reconcile_ratios

class RatioTests(unittest.TestCase):
    def test_both_zero_is_unidentifiable(self):
        self.assertEqual(poisson_ratio_interval(RatioMeasurement(0,0,100,100,1,1),.05),(0.,math.inf))
    def test_one_zero_limits(self):
        a=poisson_ratio_interval(RatioMeasurement(0,10,100,100,1,1),.05)
        b=poisson_ratio_interval(RatioMeasurement(10,0,100,100,1,1),.05)
        self.assertEqual(a[0],0.)
        self.assertEqual(b[1],math.inf)
        self.assertGreater(a[1],0.)
    def test_symmetry(self):
        a=poisson_ratio_interval(RatioMeasurement(12,33,100,180,.8,1.3),.01)
        b=poisson_ratio_interval(RatioMeasurement(33,12,180,100,1/1.3,1/.8),.01)
        self.assertAlmostEqual(a[0]*b[1],1,places=10)
        self.assertAlmostEqual(a[1]*b[0],1,places=10)
    def test_ratio_gain_bounds_expand(self):
        n=poisson_ratio_interval(RatioMeasurement(30,40,100,100,1,1),.05)
        w=poisson_ratio_interval(RatioMeasurement(30,40,100,100,.7,1.4),.05)
        self.assertLess(w[0],n[0]);self.assertGreater(w[1],n[1])
    def test_fractional_coverage_exact(self):
        # For fixed count total, exact coverage follows from binomial CIs;
        # test a finite range of N and p values numerically.
        from scipy.stats import binom
        for n in (1,3,7,14,30,100):
            for p in (.01,.1,.3,.5,.7,.9,.99):
                r=p/(1-p)
                v=sum(binom.pmf(k,n,p) for k in range(n+1) if
                      contains([poisson_ratio_interval(RatioMeasurement(k,n-k,100,100,1,1),.05)],r))
                self.assertGreaterEqual(v+1e-10,.95)
    def test_infinite_endpoint_union_sweep(self):
        out=reconcile_ratios([RatioMeasurement(0,0,10,10,1,1),
                              RatioMeasurement(3,3,10,10,1,1)],0)
        self.assertTrue(contains(out['feasible_set'],1.))
        self.assertGreater(out['feasible_set'][0][1],2.)
