#include <iostream>
using namespace std;

int main() {
	int pixHeight,percentage;
	cout<< "Enter size in pixel = ";
	cin>>pixHeight;
	percentage=(90*pixHeight)/610;
	cout<< endl << "The Size in % = ";
	cout<<percentage;
	cout<<"%"<<endl;
	return 0;
}
