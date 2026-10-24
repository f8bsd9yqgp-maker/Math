> Historical discovery checkpoint. Superseded by the complete README.md and AUDIT.md in this directory. The final rate uses time n/8 and is O((log(n)/n)^(1/4)).

# Working proof checkpoint: finite-time roughness closes the canonical limit

24 October 2026. THIS FILE IS A CHECKPOINT BEING AUDITED, not yet a final
claim. Prior results are in 2026-10-24-height-comparison. Do not rerun or
repackage them unnecessarily. The new step is below.

For an m-site ring with total mass h, let A be the average of any ell<=m
consecutive lifted heights. LA=(sum over those ell sites of d(g_i))/ell,
so 0<=LA<=K=h/ell pointwise. All height updates are increasing, and the
semigroup preserves height order. Thus v_u=P_u A is increasing and its
clock increments a_i=v_u(T_i h)-v_u(h) satisfy

    a_i>=0, sum_i a_i=L P_u A=P_u LA<=K.

In particular each a_i<=K. The Doob martingale P_(t-s) A(h(s)) has these
jumps and has terminal value A(h(t)). For lambda>=0, each sign obeys

    E exp[ +/-lambda (A(h(t))-E A(h(t))) ]
       <= exp[t(exp(lambda*K)-1-lambda*K)].

This follows by the exponential compensated-jump martingale; convexity gives
sum_i(e^(lambda*a_i)-1-lambda*a_i)<=e^(lambda*K)-1-lambda*K.
For negative lambda use e^(-z)-1+z<=e^z-1-z. The state space modulo common
vertical translations is finite, so all semigroup/generator operations are
legitimate on these affine-in-height observables.

Start at floor(phi*i), phi=h/m. Write U_i=h_i-floor(phi*i), f=E U_0.
The tilted spatial rotation of the initial heights differs from the original
by values in {0,1}; monotone coupling shows 0<=E U_j-f<=1 for every j.
Because h_i(t) is nondecreasing in i, averaging ell sites to the right and
to the left sandwiches U_0, with deterministic initial-height bias at most
phi*ell+1. Thus U_0-f is bounded above by a centered right-average plus
b=phi*ell+1 and below by a centered left-average minus b.

For any n possibly dependent copies V_i of this one-site variable, use the
2n centered average variables and log-sum-exp. If a=log(2n)<=t and K>0,
choose lambda=sqrt(a/t)/K. Since exp(z)-1-z<=z^2 for 0<=z<=1,

    E range(V_1,...,V_n) <= 2b+4K sqrt(t log(2n)).

K=0 is trivial.

Now localize an N-site balanced-start ring of density theta<=R to auxiliary
rings of size m=ceil(4t), mass h=floor(theta*m), with m<=N. For each target
site i, take auxiliary clocks from target sites i,...,i+m-1 modulo N.
Each auxiliary marginal has independent unit-rate clocks. They need not be
independent across i. Couple at the shifted target height h_(i+j)-floor(theta*i).
Before the common backward path reaches site m, its initial leaf values
differ from floor((h/m)j) by an integer in {0,1,2}. Hence |U_i-V_i|<=2.

Let D_i be the common path-reaching-m event. In both marginals D_i is exactly
{Z(t)>=m}, Z(t)~Poisson(t). Even on D_i, nonnegative increments obey
U_i<=theta*Z_target+1, V_i<=(h/m)*Z_aux. Thus

    E max_i |U_i-V_i|
       <=2+N[(theta+h/m)*t+1] P(Pois(t)>=m-1).

Consequently, for 1<=ell<=m and t>=log(2N),

    R_(N,H)(t)
     <=2R*ell+6+4R*m*sqrt(t log(2N))/ell
          +2N(2R*t+1) P(Pois(t)>=m-1).

For t>=1, m<=5t, m-1>=3t. Put c=3log(3)-2>0 and
ell=ceil((t^3 log(2N))^(1/4))<=ceil(t)<=m. Then

    R_(N,H)(t)
      <=22R*(t^3 log(2N))^(1/4)+2R+6
           +2N(2R*t+1) exp(-c*t).

At sqrt(N/2)<=t<=sqrt(N), all localization conditions hold for N>=64.
This proves the previously missing power-saving bound, if all preceding
steps survive audit. Applying the already proved cross-size comparison at
t=sqrt(n), n<=m<=2n, yields

    |q_n-q_m| <= C_R n^(-1/8) log(4n)^(1/4).

The right side is summable over successive doublings; arbitrary m>=n are
connected by doubling and one final comparison. Thus q_n is Cauchy along
all integer sizes, with the same rate up to a constant. This proves existence
of the fixed-density reduced limit, but not an exact stationary formula,
not absence of condensates, and not any interchange with finite braking.

Audit targets: semigroup commutation on affine heights; nonnegative predictive
jumps and their sum; helical left averages; phase rounding in localization;
Poisson winding identity under overlapping auxiliary rings; max-error bound;
summation of the logarithmic dyadic error. Do NOT treat simulations as proof.

AUDIT UPDATE: All new exact semigroup and localization checks passed. A stronger
choice t=n/8, for n<=m<=2n, is permitted by the roughness bound. It improves
the convergence rate to O_R((log(n)/n)^(1/4)). No power-saving assumption is
left in this argument. A final manuscript and adversarial proof audit are
being prepared; this working checkpoint is superseded by them when available.
