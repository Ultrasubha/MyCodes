#include <iostream>
using namespace std;
class Number
{
public:
	double num1,num2;
	
	Number(){						//constructor without parameter
		num1 = 0;
		num2 = 0;
	}
	
	Number(double a, double b){    //constructor with parameter
		num1 = a;
		num2 = b;
	}
	
	void showData () {
		cout << num1 << "," << num2 << endl;
	}
	
	friend Number operator - (Number&, Number&);
};


Number operator - (Number& n1, Number& n2)
{
	Number n3;
	n3.num1 = n1.num1 - n2.num1;
	n3.num2 = n1.num2 - n2.num2;
	return n3;
}
int main()
{
   
	Number temp1(4,5) , temp2(3,2) , temp3;
	temp3 = temp1 - temp2;
	
	temp3.showData();

}
