#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define sl(x) scanf("%lld", &x)
#define ps(s) printf("%s\n", s)
#define pi(x) printf("%d\n", x)
#define pl(x) printf("%lld\n", x)
#define fo(i, n) for (auto i = 0; i < n; i++)

ll jodi(ll *a, ll n, ll middle) 
{ 
    ll res = 0; 
    fo(i, n) res += upper_bound(a+i, a+n, a[i] + middle) - (a + i + 1); 
    return res;
} 

void code(){
	ll n,k; sl(n);sl(k);
	ll arr[n];
	fo(i, n) sl(arr[i]);
	sort(arr, arr+n);
    ll low = arr[1] - arr[0]; 
    fo(i, n) low = min(low, arr[i+1] - arr[i]); 
  
    ll high = arr[n-1] - arr[0]; 
  
    while (low < high) 
    { 
        ll middle = (low + high) >> 1; 
        if (jodi(arr, n, middle) < k) low = middle + 1; 
        else high = middle; 
    }
    pl(low);
}

int main() {
	ll T;sl(T);
	while(T--) code();
	return 0;
}