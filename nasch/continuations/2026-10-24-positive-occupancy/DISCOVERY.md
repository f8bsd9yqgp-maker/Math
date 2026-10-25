# Discovery checkpoint: uniform positive pile density

24 October 2026. Candidate analytic proof; the final README and audit supersede this checkpoint.

New route: use v_i=exp(lambda*(h_i-theta*i)), V=sum v_i,
and empty-block drift certificates to control W1=sum v_i 1{g_i=1}.
This is a nonstationary, pointwise generator inequality, not an assumption
about stationary mass tails.

For L>=3, L<=N, set
a=(L-3)/(L+1), b=4/[L(L+1)], m=2(L-1)/(L+1),
K=2(L-1)(L-2)/[L(L+1)],
phi_i=4/[L(L+1)] sum_{k=1}^{L-1}(L-k) 1{g_i=...=g_{i+k-1}=0}.
Then with delta=1-exp(-lambda*theta), G=sum v_i g_i, Phi=sum v_i phi_i,

 W1 <= a G + (b+K delta)V + L_generator Phi.

The positive cross term between a height jump and phi_i(T_i g)
justifies replacing sum v_i L_generator phi_i by L_generator Phi.

Also G <= [exp(lambda*theta)-1]V/lambda, and
L_generator V <= [exp(lambda*(theta-1))-exp(-lambda)]V
                 + beta W1, beta=exp(lambda)+exp(-lambda)-2.
Thus Y=V-beta Phi is positive for m beta<1 and
L_generator Y <= c Y/(1-m beta), where
c=exp(lambda*(theta-1))-exp(-lambda)
  +beta*(a*(exp(lambda*theta)-1)/lambda+b+K*delta).
It follows F_N,H<=c/[lambda*(1-m beta)].

For 0<theta<=1 and H>=2, choose L=max(3,ceil(2/theta)).
The coefficient alpha=theta*(theta-2)/2+a*theta+b <= -theta^2/6.
Elementary Taylor bounds for lambda<=1/10 give
F_N,H <=theta+alpha*lambda+8 theta lambda^2.
Choosing lambda=theta/96 yields q_N,H>=theta^3/1152.
Finite mass monotonicity extends this to q_N,H>=1/1152 when H>=N.
Consequently Q(eta)>=min(eta,1)^3/1152 for every eta>0.

This excludes a vacuum local canonical limit and complete condensation
(maximum mass/H tending to one in probability). It does NOT exclude
partial condensation, escaped mean mass, or nonergodic local limits.
No explicit formula for Q or unrestricted finite-braking NaSch is obtained.
