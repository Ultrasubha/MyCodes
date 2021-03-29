
/*
  ___________CODED BY SUBHADEEP MANDAL______________
  
  LICENSING:
  GNU General Public License v3.0  .....Dated: 29.3.2021
  (c) 2021 Guava_Slice. All rights reserved.
  
  OVERVIEW
 Shortens a name such that only initial letters and
 Surname are displayed.
  
  EXPECTATIONS
  1)Subhadeep Mandal ⇒ S.Mandal.
  2)Robert Brett Roser  ⇒ R.B.Roser.
    
  DRAWBACK
  Size of name should be less than 10 words incase name is bigger than 10
  change iteration=10 in line 28 with your preffered size
*/
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
		else							//1st Character displayed
			cout << namae[i][0] << ".";
	}	
	return 0;
}
