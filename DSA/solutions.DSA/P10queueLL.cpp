//LL operations
#include<iostream>
using namespace std;

struct node
{
	int info;
	node *link;
};
void insertAtEnd();
void deleteAtBeg();
void search();
void traverse();

node *front=NULL;
node *rear=NULL;

int main()
{
	cout<<"press 1 for insertion at the end"<<endl;
	cout<<"press 2 for deletion at the beg"<<endl;
	cout<<"press 3 for searching "<<endl;
	cout<<"press 4 for traversal"<<endl;
	cout<<"press 5 for exit"<<endl;
	
	while(1)
	{
		int ch;
		cout<<"enter choice";
		cin>>ch;
		switch(ch)
		{
			case 1:insertAtEnd();
			break;
			case 2: deleteAtBeg();
			break;
			case 3: search();
			break;
			case 4:traverse();
			break;
			case 5:exit(0);
				
		}
	}

}


void insertAtEnd()
{
	// overflow, delete node form avail, insert info to it, 
	//link it to your data LL
	//no need to check overflow by programmer
	node*temp=new node;
	cout<<"enter info";
	cin>>temp->info;
	temp->link=NULL;	
	
	if(front==NULL)
	{
		temp->link=NULL;
		front=temp;
		rear=temp;
	}
	
	else   //inserting at the end
	{
		
		rear->link=temp;
		rear=temp;
		
	}
	
}


void deleteAtBeg()
{
	if(front==NULL)
	{
		cout<<"underflow";
		return;
	}
	
	int item=front->info;
	
	node * ptr=front;
	front=front->link;
	delete ptr;
	
}

void search()
{
	int item;
	cout<<"enter item to search  ";
	cin>>item;
	
	
	node *ptr=front;
	node *loc=NULL;
	while(ptr!=NULL)
	{
		if(item==ptr->info)
		{
			loc=ptr;
			break;
		}
		
		else
		{
			ptr=ptr->link;
		}
	}
	if(loc==NULL)
	{
		cout<<"not found";
	}
	
	else
	{
		cout<<"found at  "<<loc;
	}
	
}

void traverse()
{
	node *ptr=front;
	while(ptr!=NULL)
	{
		cout<<ptr->info<<"-->";
		ptr=ptr->link;
	}
	cout<<"NULL";
}
