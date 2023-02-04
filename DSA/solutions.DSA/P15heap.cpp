//HEAP trees coding
#include<iostream>
using namespace std;
void insertion();
int deletion();
void traversal();
void sorting();
void searching();
int *a;
int n=0;
int *b;
int main()
{
	int size;
	cout<<"enter array size";
	cin>>size;
	a=new int[size];
		
	cout<<"1. insertion     2   deletion           3 traversal";
	cout<<endl<<"4.sorting       5. searching        6.exit";
while (1)
{
int z;
cout<<"Enter choice : ";
cin>>z;
switch(z)
{
case 1:
insertion();
break;
default:
cout<<"Not Valid Choice";
break;
case 2:
deletion();
break;
case 3:
traversal();
break;
case 4:
sorting();
break;
case 5:
searching();
break;
case 6:
exit(0);

}
}
}
void insertion()
{
	int item;
	cout<<"enter item";
	cin>>item;
	
	n=n+1;
	int ptr=n;
	while(ptr>1)
	{
		int par=ptr/2;
		if(item<a[par])
		{
			a[ptr]=item;
			return;
		}
		else
		{
			a[ptr]=a[par];
			ptr=par;
		}
	}
	if(ptr==1)
		a[ptr]=item;
}

int deletion()
{
int item=a[1];
int last=a[n];
int ptr=1;
n--;
int left=ptr*2;
int right=left+1;

while(right<=n)
{
	if(last>=a[left] && last>=a[right])
	{
		a[ptr]=last;
		break;
	}
	
	else if(a[left]>=a[right])
	{
		a[ptr]=a[left];
		ptr=left;
	}
	
	else
	{
		a[ptr]=a[right];
		ptr=right;
	}
	left=ptr*2;
	right=left+1;
}

if(left==n  && a[left]>last)
{
	a[ptr]=a[left];
	ptr=left;
}
else
{
	a[ptr]=last;
}

return item;
}
void traversal()
{
for(int i=1;i<=n;i++)
{
	cout<<a[i]<<"     ";
}

}
void sorting()
{
b=new int[n];
int ptr=n;
int temp=ptr;
while(ptr>=1)
{
	b[ptr-1]=deletion();
	ptr--;
	
}
for(int i=0;i<temp;i++)
{
	cout<<b[i];
}

}
void searching()
{

}


