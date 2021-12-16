/*call_by_refference is only available in cpp
  Makes the function monolithic
  should be avoided for heavy programs containing loops etc
*/
#include <stdio.h>

void swap(int &x,int &y){
    int temp=x;
    x=y;
    y=temp;
}

int main()
{
   int a=10,b=20;
   printf("a is %d and b is %d\n",a,b);
   swap(a,b);
   printf("After swapping,\na is %d and b is %d",a,b); //Value not changed
    return 0;
}
