#include <iostream>
using namespace std;
int main(){

int n;
cout<<"enter size of ARRAY";
cin>>n;
int arr[n];
for(int i=0;i<n;i++)    cin>>arr[i];
for(int i=0;i<n;i++)    cout<<arr[i]<<" ";

int value, pos;
cout<<"enter position ";
cin>>pos;
cout<< "enter value";
cin>>value;
for(int i=n;i>=pos-1;i--){
	arr[i+1]=arr[i];
}
arr[pos-1]=value;
for(int i=0;i<n+1;i++){
	cout<<arr[i]<<" ";
}
return 0;
}