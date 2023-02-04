#include <stdio.h>
#include "phone_definition.h"

int main()
{
	int iteration,lim=0;
	printf("Enter the limit\n");
	scanf("%d",&lim);
	char input[lim];
	int store[lim];
	store[0]=0;
	printf("Enter the name\n");
	
	//Taking inputs
	for(iteration=0;iteration<=lim;iteration++)
	{
		scanf("%c",&input[iteration]);
	}
	
	//Print numericals
	for(iteration=0;iteration<=lim;iteration++)
	{
		switch(input[iteration])
		{
			case 'a':
				store[iteration]=a;
				break;
			case 'b':
				store[iteration]=b;
				break;
			case 'c':
				store[iteration]=c;
				break;
			case 'd':
				store[iteration]=d;
				break;
			case 'e':
				store[iteration]=e;
				break;
			case 'f':
				store[iteration]=f;
				break;
			case 'g':
				store[iteration]=g;
				break;
			case 'h':
				store[iteration]=h;
				break;
			case 'i':
				store[iteration]=i;
				break;
			case 'j':
				store[iteration]=j;
				break;
			case 'k':
				store[iteration]=k;
				break;
			case 'l':
				store[iteration]=l;
				break;
			case 'm':
				store[iteration]=m;
				break;
			case 'n':
				store[iteration]=n;
				break;
			case 'o':
				store[iteration]=o;
				break;
			case 'p':
				store[iteration]=p;
				break;
			case 'q':
				store[iteration]=q;
				break;
			case 'r':
				store[iteration]=r;
				break;
			case 's':
				store[iteration]=s;
				break;
			case 't':
				store[iteration]=t;
				break;
			case 'u':
				store[iteration]=u;
				break;
			case 'v':
				store[iteration]=v;
				break;
			case 'w':
				store[iteration]=w;
				break;
			case 'x':
				store[iteration]=x;
				break;
			case 'y':
				store[iteration]=y;
				break;
			case 'z':
				store[iteration]=z;
				break;
			case ' ':
				store[iteration]=0;
				break;
			default:
				store[iteration]=1;
				break;

		}
	}
	
	//Printing it
	for(iteration=0;iteration<=lim;iteration++)
	{
		printf("%d ",store[iteration]);
	}
	//printf("Hello World %d",a);
}
