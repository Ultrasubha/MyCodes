#include <iostream>
using namespace std;

class numData {
	private:
		double number1 , number2;
		
	public:
	    numData (double a=0, double b=0) {
	    	this-> number1 = a;
	    	this-> number2 = b;
		}
		
		double add(double x, double y) {
			return (x+y);
		}
		
		double sub(double x, double y) {
			return (x-y);
		}
			
		double mul(double x, double y) {
			return (x*y);
		}
			
		double div(double x, double y) {
			return (x/y);
		}
		
		void printValue()
	    {
	        cout <<number1 << " + " << number2 << " = " << add(number1 , number2) << endl;
	        cout <<number1 << " - " << number2 << " = " << sub(number1 , number2) << endl;
	        cout <<number1 << " x " << number2 << " = " << mul(number1 , number2) << endl;
	        cout <<number1 << " / " << number2 << " = " << div(number1 , number2) << endl;
	        cout << endl;
	    }
};

int main() {
	
	// allocating dynamic array of Size 5 using new keyword
	numData* arr = new numData[5];
	
	// calling constructor for each index of array
	// will perform arithmatic operations of 2 consecutive integers
    for (int i = 0; i < 5; i++) {
        arr[i] = numData(i+2, i + 1);
    }
  
    // printing contents of array
    for (int i = 0; i < 5; i++) {
        arr[i].printValue();
    }
	
	return 0;
}
