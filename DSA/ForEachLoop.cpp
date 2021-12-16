#include <stdio.h>
 
int main(void) {
	int arr[5]={2,4,6,8,10};
	for (int x:arr)
		printf("%d",x);
	return 0;
}
