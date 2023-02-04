#include <stdio.h>
 
int main() {
	int a,b,c,digit,reverse,value;
	scanf("%d",&digit);
	c=digit%10;
	b=((digit-c)/10)%10;
	a=(digit-c-(b*10))/100;
	reverse = c*100+b*10+a;
	if(digit==reverse)
		printf("%d is a palindrome number",digit);
	else
		printf("%d is not a palindrome number",digit);
	return 0;
}