#include <stdio.h>
#include <stdlib.h>

struct Rectangle{
    int length;
    int breadth;
};

int main()
{
    /*STACK ALLOCATION
    struct Rectangle r={10,5};
    
    //printing directly
    printf("The length of Rectangle is %d. \n",r.length);
    printf("The breadth of Rectangle is %d. \n",r.breadth);
    
    struct Rectangle *p=&r;
    
    //printing through pointer reference
    printf("The length of Rectangle now is %d. \n",(*p).length);
    printf("The breadth of Rectangle now is %d. \n",(*p).breadth);
    */
    
    //DYNAMIC ALLOCATION (HEAP)
    struct Rectangle *p=(struct Rectangle *)malloc(sizeof(struct Rectangle));
    (*p).length = 15;
    (*p).breadth = 7;
    
    printf("The length of Rectangle is %d. \n",(*p).length);
    printf("The breadth of Rectangle is %d. \n",(*p).breadth);
    return 0;
}
