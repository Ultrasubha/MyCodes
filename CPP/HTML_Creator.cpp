//Coded By Subhadeep Mandal
#include <iostream>
#include <windows.h>
#include<fstream>
using namespace std;

int main() {
	
	HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(hConsole, 12);
	
	cout	<<	"_____________________CREATED BY SUBHADEEP MANDAL_______________________"	<<	endl	<<	endl	<<	endl;
	cout	<<	"LICENSING : "	<<	endl	<<	"GNU General Public License v3.0  .....Dated: 22.04.2021"	<<	endl;
	cout	<<	"(c) 2021 Guava_Slice. All rights reserved."	<<	endl;
	
	SetConsoleTextAttribute(hConsole, 10);
	
	ofstream file("ultra.html", ios::trunc);
	file 	<< "<!DOCTYPE html>"	<<	endl	<<	"<head>"	<<	endl	<<	"<style>"	<<	endl;
	cout 	<<		endl	<<		endl	 <<		"File Successfully Created !!!"		<<		endl;
	return 0;
}
