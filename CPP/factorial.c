#include <stdio.h>
#include <conio.h>
 
int main() {
	int digit,i,factorial;
	printf("Enter the number you want factorial of :");
	scanf("%d",&digit);
	factorial =digit;
	for (i=1;i<digit;i++)
	{
		factorial= factorial*i;
	}
	printf("The factorial is: %d\n",factorial);
 
	getch();
}
