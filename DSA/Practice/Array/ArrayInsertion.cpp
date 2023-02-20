#include <iostream>
using namespace std;
#define printArr(a) for(int i=0; i<sizeof(a)/4; i++) cout << a[i] << " ";

int main(){
    int n=9,posi= 3, val =12;
    int arr[n] = {1,2,3,4,5,6,7};
    for(int i=n-1;i>posi-2;i--)  arr[i+1] = arr[i];
    arr[posi-1] = val; 
    printArr(arr);
    return 0;
}