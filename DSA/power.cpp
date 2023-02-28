#include <iostream>
using namespace std;
#define ll long long
#define p(x) cout << x << endl

ll expo(ll x,ll n, ll M);     //T(n) = O(log(n)) space = O(1)

int main(){
    ll M = 1000000007;
    p(expo(,5, M));
    p(expo(3,10, M));
    return 0;
}

ll expo(ll x,ll n, ll M){
    ll cnt=1,val=1;
    while(n>0){
        if (n%2)    val = (val*x) % M;
        x = (x * x) % M;
        n>>=1; // dividing by 2
    }
    return val;
}