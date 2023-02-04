//Coded By Subhadeep Mandal
#include<iostream>
#include<fstream>
using namespace std;

class Employee
{
    private:
    	string name;
        int id,totalSalary;
    public:
        void setData(string a1, int b1, int c1); // Declaration
};

void Employee :: setData(string a1, int b1, int c1){
	
    name = a1;
    id = b1;
    totalSalary = c1;
    
    ofstream model("Employee_Data.bin", ios::app); // Write operation
    
    model<<"Name of Employee is : "<<name<<endl;
    model<<"ID number of "<<name<<" is : "<<id<<endl;
    model<<"TotalSalary of "<<name<<" is Rs "<<totalSalary<<endl;
    model<<endl;
}

int main(){
    Employee E1,E2,E3,E4;
    E1.setData("Joydeep",101,50000);
    E2.setData("Subhadeep",111,750000);
    E3.setData("Aman",110,40000);
    E4.setData("Manan",112,45000);
    
    string st2;

    ifstream in("Employee_Data.bin");
    for (int i = 1; i <= 15; i++) {
    	getline(in, st2);
    	
    	if(i>4 && i<12)
    		cout<<st2<<endl;
	}  
    return 0;
}

