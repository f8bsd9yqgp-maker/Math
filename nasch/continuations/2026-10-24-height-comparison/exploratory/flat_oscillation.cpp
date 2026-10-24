#include <algorithm>
#include <cmath>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>

// Finite-time samples only. No assertion about stationarity or asymptotic powers.
int main() {
    constexpr uint64_t seed = 202610240701ULL;
    std::mt19937_64 rng(seed);
    std::cout << "N,H,eta,time,samples,mean_range,se_range,mean_range_over_time,mean_height_over_time,seed\n";
    for (int n : {64,256,1024,4096,16384}) {
        int samples = n <= 4096 ? 160 : 48;
        double t = std::sqrt(n);
        std::poisson_distribution<long long> count(n*t);
        std::uniform_int_distribution<int> site(0,n-1);
        for (double eta : {0.5,1.0,1.5}) {
            int h = static_cast<int>(eta*n);
            double sum=0, sum2=0, currents=0;
            for (int rep=0; rep<samples; ++rep) {
                std::vector<int> g(n), increments(n,0);
                for (int i=0;i<n;++i) g[i]=((i+1)*h)/n-(i*h)/n;
                long long events=count(rng);
                for (long long k=0;k<events;++k) {
                    int i=site(rng), d=g[i]-(g[i]>=2);
                    g[i]-=d;
                    g[(i+n-1)%n]+=d;
                    increments[i]+=d;
                }
                auto mm=std::minmax_element(increments.begin(),increments.end());
                double range=*mm.second-*mm.first;
                sum+=range; sum2+=range*range; currents+=increments[0];
            }
            double mean=sum/samples;
            double se=std::sqrt(std::max(0.0,(sum2-sum*sum/samples)/(samples-1)/samples));
            std::cout << n << ',' << h << ',' << eta << ',' << t << ',' << samples << ','
                      << std::setprecision(12) << mean << ',' << se << ',' << mean/t << ','
                      << currents/samples/t << ',' << seed << '\n';
        }
    }
}
