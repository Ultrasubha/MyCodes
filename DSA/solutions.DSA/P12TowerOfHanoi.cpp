//TOH
#include<iostream>
#include<math.h>
using namespace std;
void TOH(int,char,char,char);
main()
{
	int n;
	cout<<"enter number of discs";
	cin>>n;
	TOH(n,'A','B','C');
	cout<<"total number of steps would be"<<(pow(2,n)-1);
}

void TOH(int n,char beg,char aux,char end)
{
	if(n==1)
	{
		cout<<beg<<"--> "<<end<<endl;
	     return;
	}
	TOH(n-1,beg,end,aux);
	cout<<beg<<"--> "<<end<<endl;
	TOH(n-1,aux,beg,end);	
}
