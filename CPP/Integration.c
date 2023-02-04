//coded by Subhadeep Mandal
#include <stdio.h>

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

//standard function
int f(int x)
{
	return x;
}

//Integration
/*int integrate(int a,int b,int h,int n)
{
	int value=0,integration,range;
	range =  b-a;
	//n*h=(b-a)
	//int integration = f(a)+f(a+h)+f(a+2h)+.....+f(a+(n-1)*h))
	for(h=0;h<n;h++)
	{
		value=value+f(x+h);
	}
	integration=value*h;
	return integration;
}*/

int main() 
{
	printf("The value is %d",f(10+2.5));
	return 0;
}

