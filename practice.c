#include <stdio.h>
#define ll long long
#define sc(x) scanf("%c", &x)
#define si(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define pc(x) printf("%c\n", x)
#define pi(x) printf("%d\n", x)
#define pl(x) printf("%lld\n", x)
#define ps(s) printf("%s\n", s)
#define repeat(n) for (int i = 0; i < n; i++)
#define fo(i, n) for (int i = 0; i < n; i++)
#define fo1(i, n, x) for (ll i = 0; i < n; i=i+x)
#define ALLOC(x, n)  (x*)malloc(n * sizeof(x));

void AddEmployee()
{
	int id,pos,i,j;
	int employee[7]={121,143,156,198,323,210};
	ps("Enter the new employee's id");
	si(id);
	ps("Enter the new employee's position");
	scanf("%d",&pos);
    pos--;
	for(i=6;i>pos;i--)
        employee[i]=employee[i-1];
	employee[pos]=id;
	
	for(j=0;j<7;j++)
        printf("The employee id is %d at position %d \n",employee[j],j+1);
}
void DelEmployee()
{
	int id,pos,i,j;
	int employee[6]={121,143,156,198,323,210};
	ps("Enter the employee's position to be deleted");
	si(pos);
	for(i=pos;i<=5;i++)
		employee[i]=employee[i+1];//employee[2]=employee[3]
	
	for(j=0;j<5;j++)
		printf("The employee id is %d at position %d \n",employee[j],j+1);
}

int main() 
{
	repeat(5) ps("hi");
    DelEmployee();
	return 0;
}