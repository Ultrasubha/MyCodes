#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main() {
	char input[100];
	strcpy(input,"learning lad rocks");
	
	fstream file("Employee_Data.txt",ios::binary | ios :: in | ios::out | ios::trunc);
	
	/*if(!file.isopen()) {
		cout << "error while opening the file";
	}*/
	

		int length = strlen(input);
		
		for(int counter = 0;counter <= length; counter++){
			file.put(input[counter]);
		}

	
	file.seekg(0);
	char ch;
	while(file.good()) {
		file.get(ch);
		cout << ch;
	}
	
	return 0;
}
