// C++ program to illustrate the
// iterators in vector
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	vector<string> g1;
	string temp;

	for (int i = 1; i < 9000; i++) {
		getline (cin,  temp);
		if(temp=="exit()")
			break;
		g1.push_back(temp);
	}

	cout << "Output of begin and end: " <<endl;
	for (auto i = g1.begin(); i != g1.end(); ++i)
		cout << *i << " ";

	return 0;
}

