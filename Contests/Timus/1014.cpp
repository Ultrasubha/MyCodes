#include <bits/stdc++.h>
using namespace std;

int main(){
    int N,x=0,y=0; cin>>N;
    if(N<10) cout<<1<<N<<endl;
    else{
        for(int i=2;i<ceil(sqrt(N));i++)
        if(N%i == 0){
            x=i;
            y=N/x;
            break;
        }
        if(!x) cout<<1<<N<<endl;
        else cout<<x<<y<<endl;
    }
    return 0;
}