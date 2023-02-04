//coded by Subhadeep Mandal
#include <iostream>
using namespace std;
 
int main() {
 
	//Considering no user will have a name more then 10 string long
	//Initialisation
	int i,iteration=10;
	string namae[10];	//name=namae in Japanese :P
 
	//Taking inputs
	cout << "Enter your full name \n";
	
	for(i=0;i<iteration;i++)
		cin >> namae[i];
 
	//Outputing shortened name
	cout << "The shortened name is \n";
	
	for(i=0;i<iteration;i++) {
 
		if(namae[i][0]>96 && namae[i][0]<123)
				namae[i][0]-=32;
 
		if(namae[i+1]=="")
			cout << namae[i];
		else
			cout << namae[i][0] << ".";
	}	
	return 0;
}
