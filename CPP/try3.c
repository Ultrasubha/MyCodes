#include <stdio.h>
 
struct student//structure tag
{
	char name[20];//members of structure
	int rn;
	float per;
};
 
int main()
{
	struct student s1={"Ravi",12,76.8};//variable of student struct
	printf("\n bytes of memory reserved for variable=%d\n",sizeof(s1));
	puts(s1.name);
	printf("\n Age of student is %d",s1.rn);
	printf("\n Percentage of student is %f",s1.per);
	return 0;
}
