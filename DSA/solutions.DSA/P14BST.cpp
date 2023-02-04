//BST
#include<iostream>
using namespace std;

struct treenode{
	treenode* left;
	int info;
	treenode *right;
};
treenode* root=NULL;

void caseA(treenode*,treenode*);
void caseB(treenode*,treenode*);

void insertion()
{
	treenode* temp=new treenode;
	
	int item;
	cout<<"enter item";
	cin>>item;
	
	temp->info=item;
	
	temp->left=NULL;
	temp->right=NULL;
	if(root==NULL)
	{
		root=temp;
		return;
	}
	else
	{
	treenode *ptr=root;
	treenode* par=NULL;
	while(ptr!=NULL)
	{
		
		if(item==ptr->info){
			cout<<"already present";
			return;
		}
		if(item<ptr->info){
		par=ptr;
		ptr=ptr->left;
		}
		
		else
		{
			par=ptr;
			ptr=ptr->right;
			}			
	}
	
	if(par->info>item)
	{
	par->left=temp;
	}
	
	else
	{
		par->right=temp;
	}
}
}

void deletion()
{
	//searching
	int item;
	cout<<"enter item to delete";
	cin>>item;
	
	treenode *ptr=root;
	treenode*loc=NULL;
	treenode*par=NULL;
	while(ptr!=NULL)
	{
		if(ptr->info==item)
		{
			loc=ptr;
			break;
		}
		
		if(item<ptr->info)
		{
			par=ptr;
			ptr=ptr->left;
		}
		
		else
		{
			par=ptr;
			ptr=ptr->right;
		}
	}   //i will get loc and par of node to be deletd
	
	if(loc->right!=NULL && loc->left!=NULL)
	{
		caseB(loc,par);
	}
	
	else
	{
		caseA(loc,par);
	}}
	
	
void caseA(treenode * loc,treenode*par)
{
	treenode* child;
	if(loc->left==NULL && loc->right==NULL)
	{
		child=NULL;
	}
	
	else if(loc->left!=NULL)
	{
		child=loc->left;
	}
	
	else
	{
		child=loc->right;
	}
	
	if(loc==par->left)
	par->left=child;
	
	else
	{
		par->right=child;
	}
	
}


void caseB(treenode * loc,treenode*par)
{
	//2 children node deletion
	//find inorder successor or predecessor
	
	//treenode *suc=loc;
	treenode *ptr=loc->right;
	treenode*parsuc=loc;
	while(ptr->left!=NULL)
	{
		parsuc=ptr;
		ptr=ptr->left;
	}
	treenode*suc=ptr;
	caseA(suc,parsuc);
	
	if(par->left==loc)
	{
		par->left=suc;
	}
	else
	{
		par->right=suc;
	}
	
	
	suc->left=loc->left;
	suc->right=loc->right;
}

void searching(){
	int item;
	cout<<"enter item";
	cin>>item;
	
	treenode *ptr=root;
	treenode*loc=NULL;
	treenode*par=NULL;
	while(ptr!=NULL)
	{
		if(ptr->info==item)
		{
			loc=ptr;
			cout<<"found at"<<ptr;
			return;
		}
		
		if(item<ptr->info)
		{
			par=ptr;
			ptr=ptr->left;
		}
		
		else
		{
			par=ptr;
			ptr=ptr->right;
		}
	}
	
	if(loc==NULL)
	{
		cout<<"not found";
	}
		
}
void inorder(treenode *ptr)    //LNR
{
	if(ptr==NULL)
	{
		return;
	}
	inorder(ptr->left);
	cout<<ptr->info<<"    "; 
	inorder(ptr->right);
}



void preorder(treenode * ptr){
	if(ptr==NULL)
	{
		return;
	}
	cout<<ptr->info<<"    "; 
	preorder(ptr->left);
	preorder(ptr->right);
}
	
void postorder(treenode * ptr)
{
	if(ptr==NULL)
	{
		return;
	}
	
	postorder(ptr->left);
	postorder(ptr->right);
	cout<<ptr->info<<"    "; 
}

	
int main()
{

	cout<<"1. insert     2  delete         3. search            4 inorder               5 preorder       6  postorder      7. exit";
	
	while(1)
	{
		cout<<"Enter your choice\n";
	int n;
	cin>>n;
	switch(n){
		case 1:
			insertion();
			break;
		case 2:
			deletion();
			break;
		case 3:
			searching();
			break;
		case 4:
			inorder(root);
			break;
		case 5:
			preorder(root);
			break;
		case 6:
			postorder(root);
			break;
		case 7:
			exit(0);
	   default:
	   	cout<<"Invalid choice\n";
	   	break;
	}}
}

