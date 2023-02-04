//Coded By Subhadeep Mandal
#include<iostream>
#include<fstream>
using namespace std;

class Employee
{
    private:
    	string carCompany;
        int cost,airbags;
    public:
        void setData(string a1, int b1, int c1); // Declaration
};

void Employee :: setData(string a1, int b1, int c1){
	
    carCompany = a1;
    cost = b1;
    airbags = c1;
    
    ofstream model("CarData.txt", ios::app); // Write operation
    
    model<<"Car Company is : "<<carCompany<<endl;
    model<<"Cost of "<<carCompany<<" is Rs "<<cost<<"Lakh"<<endl;
    model<<"The number of airbag in "<<carCompany<<" is "<<airbags<<endl;
    model<<endl;
}

int main(){
    Employee Carmodels[3];
    Carmodels[0].setData("Lamborghini",501,6); //Lamborghini Avantedor
    Carmodels[1].setData("BMW",42,6);  // BMW 3 Series
    Carmodels[2].setData("Mercedes",64,8);  //Mercedes Benz E class
    
    string strSearch;
    string compName;
    
    cout<<"Enter the Company name of your interest"<<endl;
    cin>>compName;

    ifstream in("CarData.txt");
    for (int i = 1; i <= 11; i++) {
    	getline(in, strSearch);
    	
    	if (strSearch.find(compName) != string::npos)
    		cout<<strSearch<<endl;
	}  
    return 0;
}

