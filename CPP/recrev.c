//coded by Subhadeep Mandal
#include <stdio.h>

int a,rem,rev=0;

int main() 
{
	printf("Enter a number : ");
	scanf("%d",&a);//432
	rec_reverse();
	printf("\nReverse is %d",rev);
	return 0;
}

void rec_reverse()
{
	if(a>0)//0>0
	{
		rem=a%10;//rem=4
		a/=10; //a=0
		rev=rev*10+rem;// rev=23*10+4 rev=234
	
		rec_reverse();
	}
}

