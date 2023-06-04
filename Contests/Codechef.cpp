#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vi  vector<int>
#define vll vector<long long int>
#define ll long long
#define mod 1000000007
#define inf 0x7fffffff
#define PI 3.1415926535897932384626
#define maxX(a,b) (a>b?a:b)
#define minX(a,b) (a<b?a:b)
#define isEven(a) ((a%2==0)?1:0)
#define isOdd(a) ((a%2==0)?0:1)
#define isNeg(a) ((a<0)?1:0)
#define abss(a) ((a<0)?-a:a)
#define sc(x) scanf("%c", &x)
#define si(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define pc(x) printf("%c\n", x)
#define pi(x) printf("%d\n", x)
#define pl(x) printf("%lld\n", x)
#define ps(s) printf("%s\n", s)
#define fo(i, n) for (auto i = 0; i < n; i++)
#define fo1(i, n, x) for (ll i = 0; i < n; i=i+x)
#define ALLOC(x, n)  (x*)malloc(n * sizeof(x));

typedef pair<int, int> pii;
typedef pair<ll, ll> pl;
//typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pii> vpii;
typedef vector<pl> vpl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;


ll gcd(ll a, ll b){if (a == 0) return b;   return gcd(b % a, a);}

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

ll power(ll x, ll y, ll p)
{
    ll res = 1;
    while (y > 0) {
        if (y % 2 == 1)
            res = (res * x);
        y = y >> 1;
        x = (x * x);
    }
    return res % p;
}



void solve() {
   ll n;
   sl(n);
   ll a[n];
   fo(i,n) sl(a[i]);
   vector <ll> v;
   v.push_back(1);
   for(ll i = 1; i < n-1; i++)
        if(a[i]>a[i-1] && a[i]>a[i+1])
            v.push_back(i+1);
    v.push_back(n);
    ll cnt,ans=0;
    for(ll i = 1; i < v.size(); i++) {
        cnt=v[i]-v[i-1]+1;
        ans+=(cnt*(cnt+1)/2);
    }
    ans-=(v.size()-2);
    pl(ans);
}

int main() {
    int testCase;   cin >> testCase;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    while(testCase--) solve();
    return 0;
}