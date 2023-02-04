#include <stdio.h>
#include <conio.h>

int main()
{
	int row,column,spacecount=0,range=4;
	printf("Enter the range you want :");
	scanf("%d",&range);
	for(row=1;row<=range;row++)
	{
		for(spacecount=range;spacecount>row;spacecount--)
		{
			printf("  ");
		}
		for(column=1;column<=row;column++)
		{
			printf("%d   ",column);
		}
		printf("\n");
	}
	printf("Press any key to continue...\n");
	getch();
}
