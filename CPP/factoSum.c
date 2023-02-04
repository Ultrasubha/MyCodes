#include <stdio.h>
 
int Fact(int digit);
 
int main() {
	int sum=0;
	for(int j=1;j<=4000;j++)
		sum+=Fact(j);
	
	sum%=7;
	printf("%d\n",sum);
	return 0;
}

int Fact(int digit) {
	int factorial =digit;
	
	for (int i=1;i<digit;i++)
	{
		factorial= factorial*i;
		
	}
	return factorial;
}
