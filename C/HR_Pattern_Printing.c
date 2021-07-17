//Coded by Subhadeep Mandal
//just for the records it costs 1 complete day of frustration
/*
n=7
7 7 7 7 7 7 7 7 7 7 7 7 7
7 6 6 6 6 6 6 6 6 6 6 6 7
7 6 5 5 5 5 5 5 5 5 5 6 7
7 6 5 4 4 4 4 4 4 4 5 6 7
7 6 5 4 3 3 3 3 3 4 5 6 7
7 6 5 4 3 2 2 2 3 4 5 6 7
7 6 5 4 3 2 1 2 3 4 5 6 7
7 6 5 4 3 2 2 2 3 4 5 6 7
7 6 5 4 3 3 3 3 3 4 5 6 7
7 6 5 4 4 4 4 4 4 4 5 6 7
7 6 5 5 5 5 5 5 5 5 5 6 7
7 6 6 6 6 6 6 6 6 6 6 6 7
7 7 7 7 7 7 7 7 7 7 7 7 7

n=2
2 2 2
2 1 2
2 2 2
*/
#include <stdio.h>

int main(void) {
	int i,j,n,temp,last;
	scanf("%d",&n);
	last=2*n-1;
	
	for(i=0;i<last/2;i++) {
	printf("\n");
	temp=n;
		for(j=0;j<last;j++) {
			printf("%d ",temp);
			
			if(j<last/2){
				if(j>=i)
					temp=n-i;
				else
					temp--;
			}
			else if(j>=last/2){
				if(j<last-1-i)
					temp=n-i;
				else
					temp++;
			}
		}
	}	
	
	for(i=last/2;i>=0;i--) {
	printf("\n");
	temp=n;
		for(j=0;j<last;j++) {
			printf("%d ",temp);
			
			if(j<last/2){
				if(j>=i)
					temp=n-i;
				else
					temp--;
			}
			else if(j>=last/2){
				if(j<last-1-i)
					temp=n-i;
				else
					temp++;
			}
		}
	}	
	return 0;
}
