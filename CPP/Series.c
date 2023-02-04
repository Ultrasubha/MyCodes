//coded by Subhadeep Mandal
#include <stdio.h>

//standard function
int f(int x)
{
	return x;
}
//Exponents
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

//when "first term" and "last term" provided
int sum_of_AP_uno(int n,int a,int l)
{
	int sum;
	sum=n*(a+l)/2;
	return sum;
}

//when "first term" and "common difference" provided
int sum_of_AP_bis(int n,int a,int d)
{
	int sum;
	sum=n*(2*a+(n-1)*d)/2;
	return sum;
}

//Sum of GP
int sum_of_GP(int n,int a,int r)
{
	int sum;
	sum=a*(power(r,n)-1)/(r-1);
	return sum;
}

int main() 
{
	printf("The value is %d",sum_of_GP(3,3,5));
	return 0;
}

