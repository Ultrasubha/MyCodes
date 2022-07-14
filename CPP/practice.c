#include <stdio.h>
#include <stdlib.h>
#define ll long long
#define si(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define pl(x) printf("%lld\n", x)
#define pi(x) printf("%d\n", x)
#define ps(s) printf("%s\n", s)
#define fo(i, n) for (ll i = 0; i < n; i++)
#define fo1(i, n, x) for (ll i = 0; i < n; i=i+x)
#define ALLOC(x, n)  (x*)malloc(n * sizeof(x));

ll * get_evens();
ll   add_up (ll *a, ll tillLast);
void ascification();
void dArrSum();
void code();
int main(){code();return 0;}

ll * get_evens () {                     // Function pointer returns array
    static ll nums[5];
    ll even = 0;
    fo(i, 5) nums[i] = even += 2;       // A bad way to increment
    return (nums);
}

ll add_up (ll *a, ll tillLast) {        //Passing array as parameter
   ll total = 0;
   fo(i,tillLast)   total += a[i];
   return (total);
}

void ascification(){                    //Printing ascii value of chars
    char *str = ALLOC(char,50);
	gets(str);
	for(int i=0;str[i]!='\0';i++)
		printf("%d ",str[i]);
    ps("");
    free(str);
}

void dArrSum(){
    ll size,total=0;
    sl(size);
    ll *arr = ALLOC(ll,size);

    fo(i, size) scanf("%lld",arr+i);    //Where each mem block can be accessed as *(arr+i)
    total = add_up(arr,size);

    pl(total);
    free(arr);
}

void code(){
    /*ascification();
    dArrSum();
    ll *a = get_evens();
    fo(i,5) pl(a[i]);*/
    fo1(i=2,10,2)pl(i);
}

