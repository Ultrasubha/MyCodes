#include <iostream>
#include <stdlib.h>

using namespace std;

struct Rectangle{
    int length;
    int breadth;
};

int main()
{
    Rectangle *p = new Rectangle;
    p->length = 15;
    p->breadth = 7;
    
    cout<<"The length of Rectangle is "<< p->length<<endl;
    cout<<"The breadth of Rectangle is "<< p->breadth<<endl;
    return 0;
}
