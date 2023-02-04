//Quick sort
#include<iostream>
using namespace std;
void  QS(int[],int,int);
int partition(int[],int,int);
int main()
{
	int n;
	cout<<"enter n ";
	cin>>n;
	 int *a=new int[n];
	
	cout<<"enter the elemenst  in unsorted order ";
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
	}
	
	QS(a,0,n-1);
	
	
	for(int i=0;i<n;i++)
	{
		cout<<"     "<<a[i];
	}

	return 0;
}


void QS(int x[],int beg,int end)
{
	if(beg<end)
	{
		int loc=partition(x,beg,end);
		QS(x,beg,loc-1);
		QS(x,loc+1,end);
	}

}


int partition(int a[],int beg,int end)
{
	int left=beg;
	int right=end;
	int loc=beg;
	
	//scan from right to left
	while((a[right]>=a[loc])  && (loc!=right))
	{
	right--;
   }
   
   if(loc==right)
   {
   	return loc;
   }
   
   if(a[right]<a[loc])
   {
   	int temp=a[loc];
   	a[loc]=a[right];
   	a[right]=temp;
   }
   
   loc=right;
   
   
   //scan from left to right
   	while((a[left]<=a[loc])  && (loc!=left))
	
	{
	left++;
   }
   
   if(loc==left)
   {
   	return loc;
   }
   
   if(a[left]>a[loc])
   {
   	int temp=a[loc];
   	a[loc]=a[left];
   	a[left]=temp;
   }
   
   loc=left;
}

