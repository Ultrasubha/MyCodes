#include <stdio.h>
void operation(char name[]) {
	int i,count=0;

        for(i=0;name[i]!='\0';i++)
            count=count+1;

        for(i=0;i<count;i++) {
            if(i%2==0)
                printf("%c",name[i]);
        }
        printf(" ");
        for(i=0;i<count;i++) {
            if(i%2==1)
                printf("%c",name[i]);
        }
        printf("\n");
}
int main() {
    char S[10000];
    int T;
    scanf("%d",&T);
    for(int j=0;j<T;j++){
        fflush(stdin);
    	gets(S);

		operation(S);
    }
    return 0;
}
