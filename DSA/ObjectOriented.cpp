#include <stdio.h>

class Triangle
{
    private:   //Data members
    int breadth;
    int height;

    /*Functions*/
    public:
    //Initializing with given data (Constructor)
    Triangle(int b, int h)
    {
        breadth=b;
        height=h;
    }
    
    //Just calculating the area
    float area()
    {
        return (0.5 * breadth * height);
    }
    
    //Changing a data item ((Address to structure needed to be passed))
    void changeHeight(int h)
    {
        height = h;
    }
};

int main()
{
    int mybreadth,myheight;
    
    printf("Want to calculate area of a Triangle? Pass the breath and height :");
    scanf("%d %d",&mybreadth,&myheight);
    
    
    Triangle myTriangle(mybreadth,myheight);
    printf("Area of Triangle is %.2f\n",myTriangle.area());
    
    printf("Want to change the Height? Pass the new height : ");
    scanf("%d",&myheight);
    myTriangle.changeHeight(myheight);
    
    printf("Area of Triangle now is %.2f",myTriangle.area());

    return 0;
}
