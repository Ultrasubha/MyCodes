//MErge sort
#include<iostream>
using namespace std;
void MS(int[],int,int);
void merge(int[],int,int,int);
int main()
{
	int n;
	cout<<"enter n ";
	cin>>n;
	 int a[n];
	
	cout<<"enter the elemenst  in unsorted order ";
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
	}
	
	MS(a,0,n-1);
	
	//print the final array
	for(int i=0;i<n;i++)
	{
		cout<<"    "<<a[i];
	}
	return 0;
}


void MS(int x[],int beg,int end)
{
	if(beg<end)
	{
		int mid=(beg+end)/2;
		MS(x,beg,mid);
		MS(x,mid+1,end);
		
		merge(x,beg,mid,end);
	}
}


void merge(int a[],int beg,int mid,int end)
{
	int n1=mid-beg+1;
	int n2=end-mid;
	
	int *l=new int[n1];
	int *r=new int[n2];
	
	for(int i=1;i<n1;i++)
	{
		l[i-1]=a[beg+i-1];
	}
	
	for(int j=1;j<n2;j++)
	{
		r[j-1]=a[mid+j];
	}
	
	int nll=0;
	int nr=0;
	for(int k=0;k<end;k++)
	{
		while(nll<n1  &&  nr<n2)
		{
			if(l[nll]<r[nr])
			{
				a[k]=l[nll];
				nll++;
			}
			
			else
			{
				a[k]=r[nr];
				nr++;
			}
		}
		
		
		if(nll>=n1)
		{
			while(nr<n2)
			{
					a[k]=r[nr];
					nr++;
			}
		}
		
		else
		{
			while(nll<n1)
			{
			a[k]=l[nll];
			nll++;
		}
		}
	}
}
