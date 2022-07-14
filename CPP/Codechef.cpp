#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define si(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define pl(x) printf("%lld\n", x)
#define pi(x) printf("%d\n", x)
#define ps(s) printf("%s\n", s)
#define fo(i, n) for (auto i = 0; i < n; i++)
#define fo1(i, n, x) for (ll i = 0; i < n; i=i+x)
#define ALLOC(x, n)  (x*)malloc(n * sizeof(x));

void solve() {
    int winner=1;
    ll n,sum=0;
    sl(n);
    ll arr[n];
    fo(i, n) {
        sl(arr[i]);
        if (arr[i]==1){
            winner=0;
            break;
        }
        sum+=arr[i];
    }
    if (sum%2!=0) winner=0;
    if(winner) ps("CHEFINA");
    else ps("CHEF");

}

int main() {
    int testCase = 1;
    cin >> testCase;
    while(testCase--) solve();
    return 0;
}