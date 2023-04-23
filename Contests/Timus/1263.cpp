#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,m,val;
    float f;
    cin>>n>>m;
    int arr[n]={0};
    for(int i=0;i<m;i++) {
        cin>>val;
        arr[val-1]+=1;
    }
    for(int i=0;i<n;i++) {
        f=(float)m;
        f = arr[i]*100/f;
        printf("%.2f%c\n",f,'%');
    }
    return 0;
}