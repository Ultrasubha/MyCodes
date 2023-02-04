#include <iostream>
#include <vector>
#include <windows.h>
#include <string>
#include<fstream>
using namespace std;

int main ()
{
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	
	SetConsoleTextAttribute(hConsole, 12);
	
	cout	<<	"_____________________________CREATED BY SUBHADEEP MANDAL_____________________________"	<<	endl	<<	endl	<<	endl;
	cout	<<	"LICENSING : "	<<	endl	<<	"GNU General Public License v3.0  .....Dated: 22.04.2021"	<<	endl;
	cout	<<	"(c) 2021 Guava_Slice. All rights reserved."	<< endl << endl;
	
	SetConsoleTextAttribute(hConsole, 8);
	cout	<<	"###############################    CSV MAKER     ###############################"	<< endl << endl;
	
	/*									THE	REAL FUN BEGINS									*/
	
	SetConsoleTextAttribute(hConsole, 10);
	
	vector<string> csvData;
	string data_in , choice = "No";

	cout	 << 	"PLEASE ENTER THE DATA : " 		<< 		endl 	<<	 "Type exit() anytime to stop"		<<	 endl;
	
	for(int i=1;data_in!="exit()";i++) {
		
		SetConsoleTextAttribute(hConsole, 10);
		cout	<<	i	<<	")";
		
		SetConsoleTextAttribute(hConsole, 8);
		getline (cin,  data_in);
		if(data_in=="exit()")
			break;
		csvData.push_back(data_in);
	}
	
	SetConsoleTextAttribute(hConsole, 14);
	cout	 <<		endl	<< "WOULD YOU PREFER THE DATA IN A FILE ? : " 		<< 		endl 	<<	 "(Yes/No)"		<<	 endl	<<	"Reply :	";
	getline (cin,  choice);
	cout	 <<		endl	<<	endl;
		
	if(choice == "No" || choice == "no" || choice == "NO" || choice == "") {
		
		cout	<<		"________________YOUR DATA___________________"	<<	endl	<<	endl;
		// Data will be displayed in console
		SetConsoleTextAttribute(hConsole, 13);
		for(auto i = csvData.cbegin(); i != csvData.cend(); ++i) {
			cout  <<	"\""	<<  *i		<<		"\"";
			if(i+1 != csvData.cend())
				cout	<<	",";
		}
	}
	
	else if(choice == "Yes" || choice == "yes" || choice == "YES") {
		
		string fileName;
		cout	<<	"PLEASE ENTER FILENAME : ";
		cout	<<	"(Use same file name if file is already existing and you just want to add to it.)";
		cin		>>	fileName;
		fileName += ".csv";
		ofstream file(fileName, ios::app);
		
		for(auto i = csvData.cbegin(); i != csvData.cend(); ++i) {
			file  <<	"\""	<<  *i		<<		"\"";
			if(i+1 != csvData.cend())
				file	<<	",";
		}
		
		cout	 <<		endl	<< "FILE SUCCESSFULLY CREATED !!!"	<<		endl;
	}
	
	else
		cout	<<	"INVALID CHOICE!!!"	<<	endl;
	
	SetConsoleTextAttribute(hConsole, 15);
	return 0;
}
