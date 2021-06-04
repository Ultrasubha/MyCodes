/*Suppose we are comparing implementations of insertion sort and merge sort on the
same machine. For inputs of size n, insertion sort runs in 8n2 steps, while merge
sort runs in 64n lg n steps. For which values of n does insertion sort beat merge
sort?*/

// Answer n<43
//Solution : 
#include <stdio.h>

int main(void) {
	int n=0,insertionTime,mergeTime;
	while(n<45) {
		insertionTime = 8*n*n;
		mergeTime = 64*n*log2(n);
		if(insertionTime<mergeTime)
			printf("%d ",n);
		n++;
	}
	return 0;
}
