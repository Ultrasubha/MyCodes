#include <bits/stdc++.h>
using namespace std;

int main(){
    int a,b,c,d,n; cin>>a>>b>>c>>d;
    if(a>=c) cout<<a<<endl;
    else {
        n=ceil((double)(c-a)/(double)(b+d));
        if (a+b*n > c-d*(n-1)) cout << c - d*(n-1) << endl;
        else cout << a + n*b << endl;
    }
    return 0;
}