"""Test current certificates formed from staggered folded heights."""
from fractions import Fraction as Q
from math import floor
from corrector_probe import corrector, height, gaps, compositions


def phi_integer(a, h, psi):
    return Q(sum(a),len(a))+psi[gaps(a,h)]


def phi(a, h, psi):
    cuts = sorted({Q(0), Q(1)} | {1-(x-floor(x)) for x in a if x != floor(x)})
    ans = Q(0)
    for lo,hi in zip(cuts,cuts[1:]):
        u = (lo+hi)/2
        ans += (hi-lo)*phi_integer([floor(x+u) for x in a],h,psi)
    return ans


def potential(a,n,h,psi,mode):
    cols=[sorted((Q(a[j]),Q(a[n+j])-h+Q(1,2))) for j in range(n)]
    rows=[[col[r] for col in cols] for r in range(2)]
    if mode=='min': return phi(rows[0],h,psi)
    return sum(phi(row,h,psi) for row in rows)/2


def drift(a,n,h,psi,mode):
    old=potential(a,n,h,psi,mode)
    ans=Q(0)
    for j in range(2*n):
        b=a[:]
        upper=a[(j+1)%(2*n)]+(2*h-1 if j+1==2*n else 0)
        b[j]=upper-int(upper-a[j]>=2)
        ans+=potential(b,n,h,psi,mode)-old
    return ans


if __name__=='__main__':
    for n,h in [(2,1),(2,2),(3,2),(3,3),(4,3),(4,4),(5,3)]:
        F,psi=corrector(n,h)
        worst={m:None for m in ['min','mean']}
        count=0
        for g in compositions(2*h-1,2*n):
            a=height(g)
            for m in worst:
                d=drift(a,n,h,psi,m)
                if worst[m] is None or d<worst[m][0]:worst[m]=(d,g)
            count+=1
        print({'n':n,'h':h,'states':count,'F':str(F),'worst':{m:{'drift':str(w[0]),'C':str(max(Q(0),n*(F-w[0])-Q(1,2))),'g':w[1]} for m,w in worst.items()}},flush=True)
