/*array operations
Algorithm 1 (FOR LOOP): This algo is used to traverse an array A of N elements.
1. repeat step --- for I=0 to N-1
2.do process on A[I]
3. Exit
 */
#include <iostream>
using namespace std;
		void traversal();
		void linearSearch();
		void binarySearch();
		void insertion();
		void deletion();
		void bubbleSort();
		void insertionSort();
		void selectionSort();
		void merging();
int main()
{
	cout<<"press 1 for traversal"<<endl;
	cout<<"press 2 for Linearsearch"<<endl;
	cout<<"press 3 for binry search"<<endl;
	cout<<"press 4 for insertion"<<endl;
	cout<<"press 5 for deletion"<<endl;
	cout<<"press 6 for bubble sort"<<endl;
	cout<<"press 7 for insertion sort"<<endl;
	cout<<"press 8 for selection sort"<<endl;
	cout<<"press 9 for merging"<<endl;
	cout<<"press 10 to exit"<<endl;
	
	int choice;
	cout<<"enter choice";
	cin>>choice;
	switch(choice)
	{
		case 1: traversal();
			break;
		case 2: linearSearch();
			break;
		case 3:  binarySearch();
			break;
		case 4:  insertion();
			break;
		case 5:  deletion();
			break;
		case 6:  bubbleSort();
			break;
		case 7: insertionSort();
			break;
		case 8:selectionSort();
			break;
		case 9:merging();
			break;
		case 10: exit(0);
		}
	}
}












//1. traversal

void traversal()
{	
	int a[5];
for(int i=0;i<5;i++)
cin>>a[i];

for(int i=0;i<5;i++)
cout<<a[i]<<"      ";   //only change this line with the purpose of traversal
/*if(a[i]%2==0)
cout<<"even"<<endl;
else
cout<<"odd";*/
} 















//2. linear search
void linearSearch()
{
int n;
cout<<"enter the size";
cin>>n;
int a[n];
for(int i=0;i<n;i++)
cin>>a[i];

int flag=0;
int item;
cout<<"enter item";
cin>>item;
for(int i=0;i<n;i++)
{
if(a[i]==item)
{
flag=1;
break;}
}
if(flag==0)
cout<<"element not found";
else
cout<<"found";


//using while loop && operator
int i=0;
while(i<n && a[i]!=item)
i++;
if(a[i]==item)
cout<<"element found";
else
cout<<"not found";
} 














// 3. binary search 
void binarySearch()
{
	int n;
cout<<"enter the size";
cin>>n;
int a[n];
for(int i=0;i<n;i++)
cin>>a[i];

int beg, end,mid,item;
cout<<"enter item  ";
cin>>item;

beg=0;
end=n-1;
mid=(beg+end)/2;

while(beg<=end)
{
	if(a[mid]==item)
	{
	cout<<"found at "<<mid<<"  index";
	break;
    }
    
    else if(item<a[mid])
    end=mid-1;
    
    else
    beg=mid+1;
    
    mid=(beg+end)/2;

}


//using while loop with two conditions
int beg1, end1,mid1,item1;
cout<<"enter item  ";
cin>>item1;

beg1=0;
end1=n-1;
mid1=(beg1+end1)/2;

while(beg1<=end1 && a[mid1]!=item1)
{
   if(item1<a[mid1])
    end1=mid1-1;
    
    else
    beg1=mid1+1;
    
    mid1=(beg1+end1)/2;
}
if(a[mid1]==item1)
	{
	cout<<"found at "<<mid1<<"  index";
    }
    else
    cout<<"not found";
} 













//4:insertion
void insertion()
{
int n;
cout<<"enter the size";
cin>>n;
int a[n];
for(int i=0;i<n;i++)
cin>>a[i];

int item;
cout<<"enter item to insert";
cin>>item;

//at the end
cout<<"at the end"<<endl;
a[n]=item;
n++;
for(int i=0;i<n;i++)
cout<<"    "<<a[i];
cout<<endl;

//at the beg
	cout<<"at the beg"<<endl;
	int item1;
	cout<<"enter item to insert";
	cin>>item1;
	for(int i=n-1;i>=0;i--)
	{
		a[i+1]=a[i];
	}
	a[0]=item1;
	n++;
	for(int i=0;i<n;i++)
cout<<"    "<<a[i];

//at the given index
cout<<"at the given index"<<endl;
int index;
cout<<"enter the index of insertion";
cin>>index;

int item2;
cout<<"enter item";
cin>>item2;
for(int i=n-1;i>=index;i--)
{
	a[i+1]=a[i];
	}
	a[index]=item2;
	n++;
	for(int i=0;i<n;i++)
cout<<"    "<<a[i];

//at the given position
}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	//5,deletion
		void deletion()
		{
			int n;
		cout<<"enter the size";
		cin>>n;
		int a[n];
		for(int i=0;i<n;i++)
		cin>>a[i];
		
		cout<<"at the end"<<endl;
		n--;
		for(int i=0;i<n;i++)
		cout<<"    "<<a[i];
		cout<<endl;
		
		cout<<"at the beg"<<endl;
		int temp=a[0];
		for(int i=0;i<n;i++)
		{
			a[i]=a[i+1];
		}
		n--;
		for(int i=0;i<n;i++)
		cout<<"    "<<a[i];
		cout<<endl;
		
		cout<<"at given index"<<endl;
		int index;
		cout<<"enter index";
		cin>>index;
			for(int i=index;i<n;i++)
			{
				a[i]=a[i+1];
			}
			n--;
			for(int i=0;i<n;i++)
			cout<<"    "<<a[i];
			cout<<endl;
	
}







	//6:bubble sort
		void bubbleSort()
		{
			int n;
			cout<<"enter the size";
			cin>>n;
			int a[n];
			cout<<"enter the elements in unsorted order";
			for(int i=0;i<n;i++)
			cin>>a[i];
			
			for(int pass=1;pass<n;pass++)
			{
				for(int i=0;i<n-pass;i++)
				{
					if(a[i]>a[i+1])
					{
						int temp=a[i];
						a[i]=a[i+1];
						a[i+1]=temp;
					}
				}
			}	
			for(int i=0;i<n;i++)
			cout<<"    "<<a[i];	
		}
		
	
	
	
		
		
	//7.insertion sort	
		void insertionSort()
		{
			int n;
			cout<<"enter the size";
			cin>>n;
			int a[n];
			a[0]=-1;
			cout<<"enter the elements in unsorted order and positive elements";
			for(int i=1;i<n;i++)
			cin>>a[i];
			
			
			for(int i=2;i<n;i++)
			{
				  int temp=a[i];
				  int flag=i-1;
				  while(temp<a[flag])
				  {
				  	a[flag+1]=a[flag];
				  	flag--;
				  }
				  a[flag+1]=temp;
			}
			
			for(int i=0;i<n;i++)
			cout<<"    "<<a[i];
							
		}
		
		
		
		
		
		
		
		
		
		
	//8:selection sort	
		void selectionSort()
		{	
			int n;
			cout<<"enter the size";
			cin>>n;
			int a[n];
			cout<<"enter the elements in unsorted order";
			for(int i=0;i<n;i++)
			cin>>a[i];
			
			for(int i=0;i<(n-1);i++)
			{
				int min=a[i];  
				int loc=i;
				for(int j=i+1;j<n;j++)
				{
					if(a[j]<min)
					{
						min=a[j];
						loc=j;
					}	
				}
				//swap A[i] with a[loc]
				int temp = a[i]; 
				a[i]=a[loc] ; 
				a[loc]= temp;
					}
			for(int i=0;i<n;i++)
			cout<<"    "<<a[i];
			
		}
		
		
		
		
	//9.merging
		void merging()
		{
			int r;
			cout<<"enter A size array   "<<endl;
			cin>>r;
			int a[r];
			cout<<"enter elemest to array A in sorted order";
			for(int i=0;i<r;i++)
			{
				cin>>a[i];
			}
			
			int s;
			cout<<"enter B size array   "<<endl;
			cin>>s;
			int b[s];
			cout<<"enter elemest to array B in sorted order";
			for(int i=0;i<s;i++)
			{
				cin>>b[i];
			}
			
			int n=r+s;  //c size array
			int c[n];
			int na,nb,nc;
			na=nb=nc=0;
			
			while(na<r && nb<s)
			{
				if(a[na]<=b[nb])
				{
					c[nc]=a[na];
					na++;
				}
				
				else
				{
					c[nc]=b[nb];
					nb++;
				}
				nc++;
			}
			
	
				while(nb<s)
				{
				c[nc]=b[nb];
					nb++;
					nc++;
				}
		
				while(na<r)
				{
					c[nc]=a[na];
					na++;
					nc++;
				}
			
			for(int i=0;i<n;i++)
			cout<<"    "<<c[i];	
		}
