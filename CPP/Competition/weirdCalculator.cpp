/*
  ___________CODED BY SUBHADEEP MANDAL______________
  
  LICENSING:
  GNU General Public License v3.0  .....Dated: 12.04.2021
  (c) 2021 Guava_Slice. All rights reserved.
  
  PROBLEM  
  Write a C++ program to define a class for calculator with data members as number1 and number2 
  (both as double) and methods as add(), sub(), mul(), div(). Create an array of 5 objects of 
  calculator. Use parameterized constructor to initialize the values. Display output of all four 
  arithmetic operations.
  
  OVERVIEW
  Performs Calculations of 2 consecutive integers and displays the result
  
  EXPECTATIONS
  2 + 1 = 3
  2 - 1 = 1
  2 x 1 = 2
  2 / 1 = 2

  3 + 2 = 5
  3 - 2 = 1
  3 x 2 = 6
  3 / 2 = 1.5

  4 + 3 = 7
  4 - 3 = 1
  4 x 3 = 12
  4 / 3 = 1.33333

  5 + 4 = 9
  5 - 4 = 1
  5 x 4 = 20
  5 / 4 = 1.25

  6 + 5 = 11
  6 - 5 = 1
  6 x 5 = 30
  6 / 5 = 1.2
*/

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
	
	// allocating DYNAMIC ARRAY of Size 5 using new keyword
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
