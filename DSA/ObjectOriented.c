#include <stdio.h>

//Making a demo structure with all necessary data item that might be needed for each model
struct Triangle
{
    int breadth;
    int height;
};

//initializing with given data (Address to structure needed to be passed)
void initialize(struct Triangle *t,int b, int h)
{
    t->breadth=b;
    t->height=h;
}

//Just calculating the area (Address to structure not needed to be passed)
float area(struct Triangle t)
{
    return (0.5 * t.height * t.breadth);
}

//Changing a data item ((Address to structure needed to be passed))
void changeHeight(struct Triangle *t,int h)
{
    t->height = h;
}

int main()
{
    struct Triangle myTriangle;
    int mybreadth,myheight;
    
    printf("Want to calculate area of a Triangle? Pass the breath and height :");
    scanf("%d %d",&mybreadth,&myheight);
    
    initialize(&myTriangle,mybreadth,myheight);
    
    printf("Area of Triangle is %.2f\n",area(myTriangle));
    
    printf("Want to change the Height? Pass the new height : ");
    scanf("%d",&myheight);
    
    changeHeight(&myTriangle,myheight);
    
    printf("Area of Triangle now is %.2f",area(myTriangle));

    return 0;
}
