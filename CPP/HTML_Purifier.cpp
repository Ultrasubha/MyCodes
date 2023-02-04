#include <iostream>
#include <string>
using namespace std;
int main ()
{
	string s[56];
	cout << "Please enter a string : " << endl;
	for(int i=0;i<56;i++)
		getline (cin, s[i]);
		
	cout << endl << "The states are : " << endl;
		
	for(int i=0;i<56;i++){
		if(i%2==0) {
			cout << "<option value= \"" << s[i];
			cout << "\">" << s[i] << "</option>" << endl;
		}
	}
	
	cout << endl << "The capitals are : " << endl;
		
	for(int i=0;i<56;i++){
		if(i%2!=0) {
			s[i] = s[i].substr(1, s[i].size() - 2);
			cout << "<option value= \"" << s[i];
			cout << "\">" << s[i] << "</option>" << endl;
		}
	}
	
	return 0;
}
