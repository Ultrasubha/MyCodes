//Coded by Subhadeep Mandal
//Basically my friend said a word and she wouldn't clarify it. Lets find all possible possibilities. Don't mess wid a programmar ;)
//Secret word j*i*t

#include <iostream>
using namespace std;

int main() {
	int count = 0;
	char vowels[5] = {'a','e','i','o','u'};
	
	// For first asterisk
	for(int i=0;i<5;i++)
		for(int j=0;j<5;j++) {
			count++;
			cout << count << ") " << "j" << vowels[i] << "i" <<  vowels[j] <<"t" << endl;
		}
	
	// For second asterisk
	for(int i=0;i<5;i++)
		for(int j=0;j<5;j++) {
			count++;
			cout << count << ") " << "j" << vowels[j] << "i" <<  vowels[i] <<"t" << endl;
		}
	return 0;
}
