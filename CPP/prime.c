#include<stdio.h>
#include<conio.h>
int main()
{
int i,num,flag=0;
printf("\nEnter the number");
scanf("%d",&num);//4
for(i=2;i<num;i++)
{
if(num%i==0)
{
flag=1;
break;
}
}

if(flag==0)
printf("\nPrime Number");
else
printf("\ncomposite Number");
getch();
}
