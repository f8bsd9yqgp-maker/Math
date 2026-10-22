#include <iostream>
#include <random>
#include <vector>
#include <iomanip>

// Exploratory only: no certified mixing time or stationary error bound.
// Potential null clocks are retained. uniform_int_distribution avoids modulo bias.
int main() {
  std::mt19937_64 rng(20261022);
  std::cout << std::setprecision(12);
  for(int n : {32,128,512}) {
    std::vector<int> g(n,1);
    std::uniform_int_distribution<int> site(0,n-1);
    long long count=0, one=0;
    long long two[9]={};
    const long long total=200000LL*n;
    for(long long t=0;t<total;t++) {
      int i=site(rng), j=(i+n-1)%n;
      int a=g[i]-(g[i]>=2); g[i]-=a; g[j]+=a;
      if(t>=total/2 && t%n==0) {
        count+=n;
        for(int k=0;k<n;k++) {
          one+=(g[k]>=2);
          for(int d=1;d<=8;d++)two[d]+=(g[k]>=2 && g[(k+d)%n]>=2);
        }
      }
    }
    double q=double(one)/count;
    std::cout<<"N "<<n<<" q "<<q<<" cov";
    for(int d=1;d<=8;d++)std::cout<<" "<<(double(two[d])/count-q*q);
    std::cout<<"\n";
  }
}
