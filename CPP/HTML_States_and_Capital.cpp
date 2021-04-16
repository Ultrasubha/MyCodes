/*
  ___________CODED BY SUBHADEEP MANDAL______________
  
  LICENSING:
  GNU General Public License v3.0  .....Dated: 16.4.2021
  (c) 2021 Guava_Slice. All rights reserved.
  
  OVERVIEW
  Provides a lazy way to embed codes in HTML. Just run the program put the input and copy paste the output.
  Easy Life.Lazy Life.Good Life ;)
  
  INPUT
Andhra Pradesh
(Amaravati)
Arunachal Pradesh
(Itanagar)
Assam
(Dispur)
Bihar
(Patna)
Chhattisgarh
(Raipur)
Goa
(Panaji)
Gujarat
(Gandhinagar)
Haryana
(Chandigarh)
Himachal Pradesh
(Shimla)
Jharkhand
(Ranchi)
Karnataka
(Bangalore)
Kerala
(Thiruvananthapuram)
Madhya Pradesh
(Bhopal)
Maharashtra
(Mumbai)
Manipur
(Imphal)
Meghalaya
(Shillong)
Mizoram
(Aizawl)
Nagaland
(Kohima)
Odisha
(Bhubaneshwar)
Punjab
(Chandigarh)
Rajasthan
(Jaipur)
Sikkim
(Gangtok)
Tamil Nadu
(Chennai)
Telangana
(Hyderabad)
Tripura
(Agartala)
Uttarakhand
(Dehradun)
Uttar Pradesh
(Lucknow)
West Bengal
(Kolkata)
*/

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
