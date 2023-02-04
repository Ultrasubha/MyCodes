#include <iostream>
using namespace std;

class day {	
	public:
		int date,month,year;
		
		day (int d,int m,int y) {    //constructor
			this -> date = d;
			this -> month = m;
			this -> year = y;
		}
		
		friend bool operator>(day&, day&);
};

bool operator > (day& d1 ,day& d2) {
	
	//year check
	if(d1.year > d2.year)
		return true;
		
	else if(d1.year == d2.year) {        //then we do month check
		
		if(d1.month > d2.month)
		return true;
		
		else if(d1.month == d2.month) {  //then we do day check
			
			if(d1.date > d2.date)
				return true;
			else
				return false;
		}
	
		else
			return false;
	}
	
	else
		return false;
}

void show_date(int a1, int b1,int c1,int a2,int b2,int c2) {
	
	day d1(a1,b1,c1), d2(a2,b2,c2);
	
	cout << "\n********** First Date **********" << endl;
	cout << "Date is   " << a1 << ":" << b1 << ":" << c1 << endl;
	cout << "********** Second Date **********" << endl;
	cout << "Date is   " << a2 << ":" << b2 << ":" << c2 << endl;
	
	cout << "********** Result **********" << endl;
	if(d1>d2)
		cout<<"Date " << a1 << ":" << b1 << ":" << c1  <<" is greater than "<< a2 << ":" << b2 << ":" << c2 << endl;
	else
		cout<<"Date " << a2 << ":" << b2 << ":" << c2  <<" is greater than "<< a1 << ":" << b1 << ":" << c1 << endl;
}

int main() {
	
	int date1,month1,year1,date2,month2,year2;
	
	cout <<"Enter date 1 : "<< endl << "The date = ";
	cin >> date1;
	cout << "month = ";
	cin >> month1;
	cout << "year = ";
	cin >> year1;
	
	cout << endl << "Enter date 2 : "<< endl<<"The date = ";
	cin >> date2;
	cout << "month = ";
	cin >> month2;
	cout << "year = ";
	cin >> year2;
	
	show_date(date1,month1,year1,date2,month2,year2);
	
	return 0;
}
