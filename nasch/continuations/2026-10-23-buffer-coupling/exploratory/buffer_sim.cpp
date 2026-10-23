#include <vector>
#include <random>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <cstdint>
int main(){
std::mt19937_64 gen(41731871);
for(int n: {32,128,512,2048}) {
  const int h=n,k=2;
  for(int B: {1,2,4,(int)std::ceil(std::sqrt(n)),n}) {
    std::vector<int> g(k*n,1),b={B/2,B-B/2};
    uint64_t jump=0,reads=0;double pile=0,coreBoundary=0;
    const int64_t burn=2000LL*n,steps=20000LL*n;
    for(int64_t t=-burn;t<steps;++t){
      int i=gen()%(k*n),r=i/n,j=i%n;
      int a=g[i]-(g[i]>=2);
      if(j==0){int v=std::min(a,b[r]); g[i]-=v;g[r*n+n-1]+=v;b[r]-=v;b[(r+1)%k]+=v;
        if(t>=0)jump+=v;
      }else {g[i]-=a;g[i-1]+=a;}
      if(t>=0 && t%(k*n)==0){++reads;coreBoundary+=(g[0]+g[n])/2.;
        for(int x:g)pile+=(x>=2)/(double)(k*n);}
    }
    std::cout<<n<<" "<<B<<" J "<<std::setprecision(10)<<jump*(double)n/steps<<" coreq "<<pile/reads<<" coreg0 "<<coreBoundary/reads<<"\n";
  }
}
}
