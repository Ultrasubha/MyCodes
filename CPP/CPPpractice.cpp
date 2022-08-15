#include <bits/stdc++.h>
#include <windows.h>

using namespace std;
HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);

void licensing(string name,string date) {
	char begining = 204, ending = 185;
	SetConsoleTextAttribute(hConsole, 12);
	cout	<<	"_____________________________CREATED BY SUBHADEEP MANDAL_____________________________"	<<	endl	<<	endl	<<	endl;
	cout	<<	"LICENSING : "	<<	endl	<<	"GNU General Public License v3.0  .....Dated: "<<	date	<<	endl;
	cout	<<	"(c) 2021 Guava_Slice. All rights reserved."	<< endl << endl;
	SetConsoleTextAttribute(hConsole, 8);
	cout	<<	"###############################    "	<<	begining	<<	name	<<	ending	<<		"     ###############################"	<< endl << endl;
	SetConsoleTextAttribute(hConsole, 10);
}

int main (){
	licensing(" Let\'s Create ","02-05-2021");
	return 0;
}
