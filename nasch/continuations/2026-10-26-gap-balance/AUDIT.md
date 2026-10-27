# Audit of continuation 21

## Analytic claims

1. For N>=2, any H>=0, and any full-model stationary law,
   the mean velocity satisfies the finite-M bound (5) in README.
   For H/N<=R and 0<epsilon<=1/2 this gives
   `U<=(3+6R)epsilon^(1/3)`, independently of road size.
2. The same proof works for translation-invariant stationary laws on
   the infinite car-label line with finite mean gap.
3. For H<2N, resting-gap projection changes at most twice the number
   of changed input coordinates. One changed coin consequently changes
   at most four projected gaps.
4. Mixed marked coins have conditional expectation at most
   `epsilon m+2epsilon b/(1-epsilon)`. Charging these coins gives the
   explicit cylinder-generator error (2) in LOCAL_STATIONARY_REDUCTION.
5. Every bounded-density zero-noise local limit is resting; in the
   project's eta<2 range its gap law is backchip-stationary without a
   restriction on epsilon N. It need not have mean eta or be uniquely
   selected by eta on the basis of the present proof.

The proofs are analytic. Finite checks support the local algebra and
implementation; they are not evidence by extrapolation for a limit.

## Checks completed

| Script | New checks | Status |
| --- | --- | --- |
| verify.py | 12,900,352 deterministic threshold tests in 529,232 state/mask cases; 44,091 exact rational constant checks | Passed |
| verify_local_reduction.py | 39,024 projected comparisons; 179,168 one-coin Hamming checks; 3,360 seeded projection perturbations; 756 exact conditional mixed-coin expectations | Passed |
| same independent script | 291,452 threshold checks and 5,280 block-drift checks including larger H>=2N cases | Passed |
| verify_cylinders.py | 75,072 exact resting-cylinder expansion checks; 1,840 escaped-mass obstruction checks | Passed |
| verify_flow_fixtures.py | 20 rational Bernstein certificates on the full interval 0<=epsilon<=1/2, using four archived full-model flows | Passed |

The first script reuses only the earlier composition generator and original
one-step update. The local-reduction script separately implements the
original four NaSch steps and computes projection by repeated full braking,
rather than using the formula it audits. Its small cases are exhaustive;
its larger cases use a recorded random seed and exact integer arithmetic.
Seeded examples are tests, not statistical confidence statements.
The cylinder script uses this independent direct projection implementation.
The fixture script imports only archived rational formulas and polynomial
arithmetic. No older stationary, first-passage, or Poisson solver was rerun.

## Manual audit points

- Fresh adjacent coins are independent only for N>=2. The N=1 extension
  is false and explicitly excluded.
- The block-work proof, unlike deterministic resting projection, works
  even when every car is qualified. The velocity theorem therefore
  allows H>=2N; the projected reduction still assumes H<2N.
- Stationarity of a bounded pair-threshold indicator gives births equal
  losses. The proof drops additional losses and only enlarges births.
  It does not assume independent gaps or qualifications.
- On a ring the number of 01 and 10 pairs is equal pathwise. On the
  infinite line equality follows from translation invariance.
- Infinite-volume block work is an integrable single-site observable;
  no infinite sum or second-moment assumption is used there.
- Original and projected laws need not define a Markov projection.
  Equal one-time distributions suffice for the stationary expectation.
- The serialization error counts nearby marked pairs before averaging;
  no independence between serialization order and mask is assumed.
- Passing generator equations to the limit uses bounded cylinder
  observables. A short-time Dynkin expansion supplies the separate
  infinitesimal-invariance-to-invariance step.
- The conclusions about local limits require cyclic averaging if the
  finite stationary laws have not been assumed translation invariant.
- The word "uniform" concerns explicit estimates in N. It does not
  establish a fixed-positive-epsilon thermodynamic limit.

## Dependencies and scholarly status

The velocity proof is self-contained apart from the elementary exact
traffic update, which is displayed. The local reduction uses the earlier
deterministic relaxation and serialization lemmas; their key formulas
and the required consequences are stated and their new uses audited.
The reduced-phase classification is invoked only in a separately labelled
interpretation after the new stationarity theorem has been proved.

Previous result: the reduced scalar Q converges along all size sequences.
New result: the full zero-noise local gap limit is reduced-stationary.
Unproved identification: this local gap law is the canonical reduced law
at the prescribed density, with the correct first-order full current.

Independent specialist peer review, formal verification, and priority
verification remain outstanding. The full stationary-flow problem is not
claimed solved.

## Reproduction

From this directory, with Python 3.9+ and the standard library:

```sh
python3 verify.py
python3 verify_local_reduction.py
python3 verify_cylinders.py
python3 verify_flow_fixtures.py
```

Each script writes its exact result in results/. MANIFEST.json records
SHA-256 hashes for the proof, audit, code, and results files.
