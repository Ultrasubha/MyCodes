#include <stdio.h>

int power(int number,int power)
{
	int i=1,result;
	result=number;
	while(i<power)
	{
		result=number*result;
		i++;
	}
	return result;
}

int main() 
{
	int num,pow;
	printf("Enter the digit and the exponent value sequencially :");
	scanf("%d %d",&num,&pow);
	printf("The value is %d",power(num,pow));
	return 0;
}

