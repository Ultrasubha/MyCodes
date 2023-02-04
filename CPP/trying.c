//date of birth 12/12/1998
#include<stdio.h>

struct student
{
char name[20];
int roll;
struct dob
{
int day,month,year;
}d;//variable of inner struct(dob)
};
int main()
{

struct student s1;//variable of outer struct(student)
printf("\nEnter name : ");
scanf("%s",s1.name);
printf("\nEnter roll number : ");
scanf("%d",&s1.roll);
printf("\nChecking Date of Birth : \n");
printf("\nEnter day : ");
scanf("%d",&s1.d.day);
printf("\nEnter month : ");
scanf("%d",&s1.d.month);
printf("\nEnter year : \n");
scanf("%d",&s1.d.year);
//printf("%d",sizeof(s1));//36
//printf("%d",sizeof(s1.d));//12

puts(s1.name);
printf("\nRoll Number is %d",s1.roll);
printf("\nDate of birth %d/%d/%d",s1.d.day,s1.d.month,s1.d.year);
return 0;
}
