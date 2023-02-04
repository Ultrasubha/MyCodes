/* 4 types of fucntion based on argument and return types:
1. no argument no return type
2. no argument with return type
3. with argument ,no eturn type
4. with argument, with return type
*/
#include<iostream>
using namespace std;

//no arg no ret type
void sum1();  //declaration
void sum1()    //defination
{
	cout<<"hey i am NANR-> not getting anything from call in the form of argument,not giving anything back to call in the form of return type"<<endl;
	int a=9; int b=10;
	int c=a+b;
	cout<<"the sum,  staying inside the body of sum1  ,is"<<c;
	cout<<endl;
	cout<<endl;
}


//no argument with return type
float sum2(); //declaration
float sum2()  //defination
{
	cout<<"I am NAWR-> not getting anything from the call in the form of argument but returning a value back to call,so call must have a variable to catch the returned value"<<endl;
	float a=90.8;
	float b=4.5;
	float c=a+b;
	return c;
}


//with argument no return type
void sum3(double ,int);    //declaration
void sum3(double a, int b)    //defination
{
	cout<<"hey i am WANR:taking values from the call in the form of argument but not returning anything back to call."<<endl;
	double c=a+b;
	cout<<"the sum,   staying inside the body of sum3  ,  is"<<c;
	cout<<endl;
	cout<<endl;
}


//With argument with return type
float sum4(float ,int);    //declaration
float sum4(float a, int b)   //defination
{
	cout<<"I am WAWR:getting the values from the call in the form of argument and also giving back the value to the call in the form of return statement"<<endl;
	return (a+b);
}


 main()
{
	
sum1(); //NANR
	
	
float catch1=sum2();  //NAWR	
cout<<"the sum, as a passed value from defination to call of sum2   , is"<<catch1;
cout<<endl;
cout<<endl;

sum3(45.5,20);    //WANR


float x=8.8;   //WAWR
int y=9;
float catch2=sum4(x,y);     
cout<<"the sum , as a passed value from defination to call of sum4   , is"<<catch2;
cout<<endl;
cout<<endl;
}


