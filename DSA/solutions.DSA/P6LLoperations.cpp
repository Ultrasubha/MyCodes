//LL operations
#include<iostream>
using namespace std;

struct node
{
	int info;
	node *link;
};
void insertAtBeg();
void insertAtEnd();
void insertInSortedLL();
void deleteAtBeg();
void deleteAtEnd();
void deleteInSOrtedLL();
void searchInUnsortedLL();
void searchInSortedLL();
void traverse();

node *start=NULL;

int main()
{
	cout<<"press 1 for insertion at the beg"<<endl;
	cout<<"press 2 for insertion at the end"<<endl;
	cout<<"press 3 for insertion in sorted LL"<<endl;
	cout<<"press 4 for deletion at the beg"<<endl;
	cout<<"press 5 for deletion at the end"<<endl;
	cout<<"press 6 for deletion in sorted LL"<<endl;
	cout<<"press 7 for searching in unsorted LL"<<endl;
	cout<<"press 8 for searching in sorted LL"<<endl;
	cout<<"press 9 for traversal"<<endl;
	cout<<"press 10 for exit"<<endl;
	
	while(1)
	{
		int ch;
		cout<<"enter choice";
		cin>>ch;
		switch(ch)
		{
			case 1:insertAtBeg();
			break;
			case 2: insertAtEnd();
			break;
			case 3: insertInSortedLL();
			break;
			case 4: deleteAtBeg();
			break;
			case 5: deleteAtEnd();
			break;
			case 6: deleteInSOrtedLL();
			break;
			case 7: searchInUnsortedLL();
			break;
			case 8: searchInSortedLL();
			break;
			case 9:traverse();
			break;
			case 10:exit(0);
				
		}
	}

}


void insertAtBeg()
{
	// overflow, delete node form avail, insert info to it, 
	//link it to your data LL
	//no need to check overflow by programmer
	node*temp=new node;
	cout<<"enter info";
	cin>>temp->info;
	if(start==NULL)
	{
		temp->link=NULL;
		start=temp;
	}
	
	else   //inserting at the beginning
	{
		temp->link=start;
		start=temp;
	}
	
}

void insertAtEnd()
{
	node *temp=new node;
	cout<<"enter item  ";
	cin>>temp->info;
	node *ptr=start;
	while(ptr->link!=NULL)
	{
		ptr=ptr->link;
	}
	
	temp->link=NULL;
	ptr->link=temp;
	
}
void insertInSortedLL()
{
	int item;
	cout<<"enter item ";
	cin>>item;
	
	node *temp=new node;
	temp->info=item;
	
	if(start->info>item)
	{
		temp->link=start;
		start=temp;	
		return;
	}
	
	node *copy=start;
	node *ptr=start->link;
	while(ptr!=NULL)
	{
	 if(item>ptr->info)
	{
		copy=ptr;
		ptr=ptr->link;
		break;
	}
}
 
 temp->link=copy->link;
 copy->link=temp;
}

void deleteAtBeg()
{
	if(start==NULL)
	{
		cout<<"underflow";
		return;
	}
	
	int item=start->info;
	
	node * ptr=start;
	start=start->link;
	delete ptr;
	
}
void deleteAtEnd()
{
node *locp;
node *ptr=start;
while(ptr->link!=NULL)
{
	locp=ptr;
	ptr=ptr->link;
}
locp->link=ptr->link;
delete ptr;
}


void deleteInSOrtedLL()
{
	int item;
	cout<<"enter item you want to delete ";
	cin>>item;
	
	if(item < start->info)
	{
		cout<<"not present";
		return;
	}
	
	node * locp=start;
	node *ptr=start->link;
	while(ptr!=NULL)
	{
		if(item<ptr->info)
		{
			cout<<"not present ";
			return;
		}
		
		else if (item==ptr->info)
		{
			locp->link=ptr->link;
			break;
		}
		
		else
		{
			locp=ptr;
			ptr=ptr->link;
		}
		
	}
	
}
void searchInUnsortedLL()
{
	int item;
	cout<<"enter item to search  ";
	cin>>item;
	
	
	node *ptr=start;
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
void searchInSortedLL()
{
	
}

void traverse()
{
	node *ptr=start;
	while(ptr!=NULL)
	{
		cout<<ptr->info<<"-->";
		ptr=ptr->link;
	}
	cout<<"NULL";
}
