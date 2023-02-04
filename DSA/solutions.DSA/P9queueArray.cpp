/* Queue:based on FIFO
4 operatiosn on queue: enqueue ,dequeue,search, travers

QUEUE Array */
/*Stack operation: work on LIFO, 
There are 4 operation on stack: push, pop, traversal,searching

STACK ARRAY*/
#include <iostream>
using namespace std;
void enqueue();
void dequeue();
void traversal();
void searching();

int *queue;
int front=-1;
int rear=-1;
int size;
int main()
{
	cout<<"enter size of the array  ";
	cin>>size;
	queue=new int[size];
	
	while(1)
	{
		int n;
		cout<<"Enter the operation code : ";
		cin>>n;
		switch(n)
		{
			case 1 :
			enqueue();
			break;
			case 2 :
			dequeue();
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
		void enqueue()
		{
			int item;
			cout<<"enter item ";
			cin>>item;
			
		if((front==0 && rear==size-1) || (front==rear+1))
		{
			cout<<"overflow";
			return;
		}
		
		if(front==-1)
		{
			front=rear=0;
		}
		
		else if(rear==size-1)
		{
			front=rear=0;
		}
		else
		{
			rear++;
		}
		queue[rear]=item;	
		}
		void dequeue()
		{
		int item=queue[front];
		if(front==-1)
		{
			cout<<"underflow";
			return;
		}
		
		else if( front==rear)
		{
			front=rear=-1;
		}
		
		else if(front==size-1)
		{
			front=0;
		}
		
		else
		{
			front++;
		}
		
		}
		void traversal()
		{
			int ptr=front;
			while(ptr<=rear)
			{
				cout<<queue[ptr]<<"   ";
				if(front!=-1 && front==size-1)
				{
					front=0;
				}
				
				else
				ptr++;
			}
		
		}
		void searching()
		{
			
			int item;
			cout<<"enter item to search";
			cin>>item;
			int flag=0;
			int ptr=front;
			while(ptr<=rear)
			{
				if(item==queue[ptr])
				{
					flag=ptr;
					break;
				}
				if(front!=-1 && front==size-1)
				{
					front=0;
				}
				
				else
				ptr++;
			}
			if(flag==0)
			{
				cout<<"not found";
			}
			
			else
			{
				cout<<"found at "<<flag;
			}
	
		}
		
		

