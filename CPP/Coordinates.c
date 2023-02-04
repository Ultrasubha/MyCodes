#include<stdio.h>

int co1[11][11],row,column,lim=10;

int main()
{
	frame_triangle();
	//show_yAxis();
	//show_xAxis();
	return 0;
}

frame()
{
	int i;
	
	for(row=lim;row>=0;row--)
	{
		for(column=0;column<=lim;column++)
		{
			co1[row][column]=row*column;
		}
	}
	
	//Correcting the axis
	for(i=0;i<=lim;i++)
	{
		co1[0][i]=i;
		co1[i][0]=i;
	}
}

show()
{
	printf("\n\n                            GEOMETRIC SHAPE WITH ARRAYS\n\n\n\n");
	
	for(row=lim;row>=0;row--)
	{
		for(column=0;column<=lim;column++)
		{
			printf("%d\t",co1[row][column]);
		}
		printf("\n\n");
	}
}

show_xAxis()
{
	int i;
	for(i=0;i<=lim;i++)
	{
		printf("%d\t",co1[0][i]);
	}
}

show_yAxis()
{
	int i;
	for(i=lim;i>0;i--)
	{
		printf("%d\n\n",co1[i][0]);
	}
}

frame_triangle()
{
	int i,a=lim;
	
	for(row=lim;row>=0;row--)
	{
		for(column=0;column<=lim;column++)
		{
			co1[row][column]=1111111;
		}
	}
	
	for(i=0;i<=lim;i++)
	{
		co1[0][i]=0;
		co1[i][0]=0;
		co1[a][i]=0;
		a--;
	}
	show();
}
