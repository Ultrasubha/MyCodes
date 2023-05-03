#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,k,surv=0,boom,left=0;
    cin>>n>>k;
    for(int i=0;i<n;i++) {
        cin>>boom;
        if (boom<k) surv += k-boom;
        else left += boom-k;
    }
    cout<<left<<" "<<surv;
    return 0;
}