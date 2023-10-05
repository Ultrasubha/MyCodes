#include<stdio.h>
#include<stdlib.h>

int main(){
    int cnt=0,num=0;
    int* ptr = (int*) calloc(1, sizeof(int));
    while(4<5){
        scanf("%d\n", &ptr[cnt]);
        cnt++;
        for(int i=0; i<cnt; i++){
            printf("%d ",ptr[i]);
        }
        ptr = (int*) realloc(ptr, (cnt+1) * sizeof(int));
    }
    free(ptr);
    printf("adfad");
    return 0;
}