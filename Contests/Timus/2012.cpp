#include <bits/stdc++.h>
using namespace std;

int main()
{
    int pr; cin>>pr;
    int r=12-pr;
    int minutes=(4*60)-r*45;
    cout<<(minutes>=0?"YES\n":"NO\n");
    return 0;
}