#include <iostream>
using namespace std;
#define printArr(a) for(int i=0; i<sizeof(a)/4; i++) cout << a[i] << " ";

int main(){
    int n=7,posi= 3;
    int arr[n] = {1,2,3,4,5,6,7};
    for (int i=posi-1;i<n;i++) arr[i] = arr[i+1];
    arr[n-1] = 0;
    printArr(arr);
    return 0;
}