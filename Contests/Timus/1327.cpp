#include<bits/stdc++.h>
using namespace std;


int main() {
    int a,b; cin>>a>>b;
    if (a&1 || b&1) cout<< (b-a)/2+1 << endl;
    else cout<< (b-a)/2 << endl;
    return 0;
}