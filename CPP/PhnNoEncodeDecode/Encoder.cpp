//coded by Subhadeep Mandal
//at
//https://ideone.com/fDrzqF

#include <iostream>
using namespace std;

int main() {
	long int phn,firstDigit; //Cuz phone number be big
	short int rem; //Short cuz I am a memory freak
	cin>>phn;
	
	firstDigit=phn;
  
  //Extracting first number
	while(firstDigit>10)
		firstDigit/=10;
	
  //Generating the Desired output
	cout<<firstDigit;
	while(phn>10){
		rem=phn%10;
		phn/=10;
		cout<<firstDigit-rem;
	}
	return 0;
}
