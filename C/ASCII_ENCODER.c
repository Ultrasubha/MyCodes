/*
PROGRAM TO ENCODE A SENTENCE WITH ASCII
CREATED BY SUBHADEEP MANDAL
DATE: 30/12/2021
*/
#include <stdio.h>

int main(void) {
	char str[500];
	gets(str);
	for(int i=0;str[i]!='\0';i++)
		printf("%d ",str[i]);
	return 0;
}
