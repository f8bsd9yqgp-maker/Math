# Continue here: positive pile density and critical mass-loss structure

24 October 2026. Do not restart the scalar convergence proof. It was already
published in 914102c5840511b8f97da0640ec30ade81c069e0. Read README.md and
PHASE_SELECTION.md here, then AUDIT.md. All new proofs are internally
audited AI-assisted mathematics, not independently peer reviewed.

## Newly proved

* For N>=3,H>=2: q_(N,H)>=min(H/N,1)^3/1152.
* Hence Q(eta)>0 at every eta>0. No vacuum local canonical limit, and no
  complete condensation M_N/H_N->1 in probability.
* The sharper rational specialization gives q_(N,N)>=3783923/824263923>1/218.
* Every existing deterministic finite-density stationary phase has pile
  probability Q at its own density. This follows by the flat-line speed
  limit and an L1 ergodic initial-height comparison.
* Define r(a)=largest argmax_(r>=0)[Q(r)-a*r], a>0. At each positive r(a)
  the whole canonical law converges to the unique phase of that density,
  and masses are uniformly integrable.
* Let eta_c=lim_(a down to0) r(a). Then eta_c>1/217. Canonical masses are
  uniformly integrable at every finite eta<=eta_c, so max mass/N->0 in
  probability there. This includes the explicit interval (0,1/217].
* Q is strictly increasing up to eta_c, so no intermediate plateau is possible.
* If eta_c is finite, it is the first permanent plateau density of Q.
  The whole local canonical law at every eta>=eta_c converges to the
  unique critical phase of mean eta_c. Escaped mean is exactly eta-eta_c.

## Key new algebra

v_i=exp(lambda*(h_i-theta*i)), V=sum v_i, G=sum v_i*g_i,
P=sum v_i*1{g_i=1}; weights are periodic.

sum v_i exp(lambda*g_i)=exp(lambda*theta)V;
G<=(exp(lambda*theta)-1)V/lambda;
sum(v_i-v_(i-1))_+<=(1-exp(-lambda*theta))V.

For 3<=ell<=N,
a=(ell-3)/(ell+1), b=4/[ell(ell+1)],
m=2(ell-1)/(ell+1), K=2(ell-1)(ell-2)/[ell(ell+1)],
phi_i=4/[ell(ell+1)] sum_(k=1)^(ell-1)(ell-k)e_(i,k), 0<=phi<=m.

The exact empty-block generator plus telescoping gives
P<=aG+(b+K delta)V+sum v_i L phi_i, delta=1-exp(-lambda*theta).
The jump-product term is nonnegative, so sum v_i L phi_i<=L(sum v_i phi_i).
With beta=exp(lambda)+exp(-lambda)-2,
Y=V-beta sum v_i phi_i is positive for m beta<1 and
L Y <= [A+beta B]Y/(1-m beta),
A=exp(lambda*(theta-1))-exp(-lambda),
B=a*(exp(lambda*theta)-1)/lambda+b+K delta.
This bounds stationary F by [A+beta B]/[lambda*(1-m beta)].
Choose ell=max(3,ceil(2/theta)), lambda=theta/96 for theta<=1,H>=2;
then q>=theta^3/1152. Use finite mass order above density one.

## Critical selection mechanism

For any canonical limit at eta, its random phase density R obeys
E R<=eta and E Q(R)=Q(eta). At eta=r(a), the global supporting line
Q(r)<=a*r+b makes
0=a*(eta-E R)+E[aR+b-Q(R)].
Both terms are nonnegative. R is supported on maximizers, all <=eta,
and has mean eta, so R=eta. This proves existence and selection there.
Stochastic domination then propagates uniform integrability to lower
canonical densities. The endpoint uses a Lipschitz tail comparison.
The finite plateau case uses strict identification of ordered stationary
laws by q to select the same critical local law at all larger densities.

## Do not overclaim

It remains unknown whether eta_c is finite or infinite. Uniform
integrability alone does not select a phase at every density below eta_c.
No explicit Q, full arbitrary-density canonical distribution, original
T_N formula, limit interchange, or unrestricted finite-braking NaSch
stationary formula has been proved. The strongest new conclusions are
positivity, mass retention on a definite interval and up to the intrinsic
critical endpoint, and the conditional saturation classification.

## Audit

New standard-library verifier: 3,276 empty-block generator checks;
2,972 weighted rational certificates; 19,899 rounding/alpha checks;
eight rigorous exponential-enclosure bounds; exact density-one logarithm
certificate. All passed. No old verifier or stationary solver was rerun.
The final proof follows the complete algebra in README.md and the analytic
selection argument in PHASE_SELECTION.md, not the finite samples.
