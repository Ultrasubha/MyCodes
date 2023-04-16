#include<bits/stdc++.h>
using namespace std;

int main(){
    int N,cnt=0; cin>>N;
    int arr[N];
    for(int i=0; i<N; i++) cin>>arr[i];
    for(int j=0; j<N; j++) {
        if(cnt==0) cnt++;
        if(arr[j]==arr[j+1]) cnt++;
        else {
            cout<<cnt<<" ";
            cout<<arr[j]<<" ";
            cnt=0;
        }
    }
    return 0;
}