/*Stack operation: work on LIFO, 
There are 4 operation on stack: push, pop, traversal,searching

STACK ARRAY*/
#include <iostream>
using namespace std;
void push();
void pop();
void traversal();
void searching();

int *stack;
int top=-1;
int size;
int main()
{
	cout<<"enter size of the array  ";
	cin>>size;
	stack=new int[size];
	
	while(1)
	{
		int n;
		cout<<"Enter the operation code : ";
		cin>>n;
		switch(n)
		{
			case 1 :
			push();
			break;
			case 2 :
			pop();
			break;
			case 3 :
			traversal();
			break;
			case 4 :
			searching();
			break;
			case 5: exit(0);
		}
	}
}
		void push()
		{
			if(top==size-1)
			{
				cout<<"overflow";
				return;
			}
			
			top++;
			cout<<"enter item";
			cin>>stack[top];
			
			//OR   cin>>stack[++top];
		
		}
		void pop()
		{
			if(top==-1)
			{
				cout<<"underflow";
				return;
			}
			int item=stack[top];
			top--;
		
		}
		void traversal()
		{
			int ptr=top;
			while(ptr!=-1)
			{
				cout<<"        "<<stack[ptr]<<"    ";
				ptr--;
			}
		
		}
		void searching()
		{
		int item;
		cout<<"enter item  ";
		cin>>item;
		
		int ptr=top;
		int loc=0;
		while(ptr!=-1)
		{
			if(stack[ptr]==item)
			{
				loc=ptr;
				break;
			}
			
			else
			{
				ptr--;
			}
		}
		if(loc==0)
		{
			cout<<"not found";
		}
		else
		{
			cout<<"found at  "<<loc;
		}
		}
		
		

