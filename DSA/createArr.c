#include <stdio.h>
#include <stdlib.h>

int * createArray(int size){
    int *p = (int *)malloc(size*sizeof(int));
    return p;
}

int main()
{
   int *arr = createArray(5);
   for(int i=0;i<5;i++){
       *(arr+i) = 5*i;
        printf("%d) %d\n",i,*(arr+i));
   }
    return 0;
}
