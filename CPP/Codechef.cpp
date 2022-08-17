#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vi  vector<int>
#define vll vector<long long int>
#define si(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define pl(x) printf("%lld\n", x)
#define pi(x) printf("%d\n", x)
#define ps(s) printf("%s\n", s)
#define fo(i, n) for (auto i = 0; i < n; i++)
#define fo1(i, n, x) for (ll i = 0; i < n; i=i+x)
#define ALLOC(x, n)  (x*)malloc(n * sizeof(x));

void bubbleSort(ll arr[], ll n) {
   ll i, j;
   bool swapped;
   for (i = 0; i < n-1; i++) {
     swapped = false;
     for (j = 0; j < n-i-1; j++) {
        if (arr[j] > arr[j+1]) {
           swap(arr[j], arr[j+1]);
           swapped = true;
        }
     }
     if (swapped == false)
        break;
   }
}

ll factorial(ll num) {
   if(num==0) return 1;
   return num * factorial(num -1);
}

ll gcd(ll a, ll b)
{
    if (a == 0)
        return b;
    return gcd(b % a, a);
}

void solve() {
   ll n; sl(n);
   ll arr[n];
   fo(i, n) sl(arr[i]);
   ll sudhint,val=2512199;
   string s="";
   cin>>s;
   fo(i,s.length()){
      sudhint=(int)s[i]-48;
      if(sudhint==0)
         if(arr[i]<=val || val==2512199)
            val=arr[i];
   }
   pl(val);
}

int main() {
    //int testCase = 1;
    //cin >> testCase;
    //while(testCase--) solve();
    cout<< gcd(14,16) << endl;
    return 0;
}