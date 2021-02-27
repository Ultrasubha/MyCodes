//coded by Subhadeep Mandal
#include <iostream>
using namespace std;

int main() {
	
	//Considering no user will have a name more then 10 string long
	//Initialisation
	int i,iteration=10;
	string namae[10];	//name=namae in Japanese :P
	
	//Taking inputs
	for(i=0;i<iteration;i++)
		cin >> namae[i];
	
	//Outputing shortened name
	for(i=0;i<iteration;i++) {
		
		//If a nincompoop writes his name in small this will fix the issue
		if(namae[i][0]>96 && namae[i][0]<123)
				namae[i][0]-=32;
		
		if(namae[i+1]=="")					//displayed full
			cout << namae[i];
		else								//1st Character displayed
			cout << namae[i][0] << ".";
	}	
	return 0;
}
