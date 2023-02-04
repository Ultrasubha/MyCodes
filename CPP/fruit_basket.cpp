#include <iostream>
using namespace std;

int main()
{
  int TestCases,Apple,Banana,Mango,count;
  bool eaten;
  cin>>TestCases;

  for(int i=0;i<TestCases;i++){

        cin>>Apple>>Banana>>Mango;

        count=0;
        eaten=true;
        while(eaten==true){
	        if(Apple!=0 && Banana!=0){
	            Apple--;
	            Banana--;
	            count++;
	            eaten=true;
	        }
	
	        else if(Banana!=0 && Mango!=0){
	            Banana--;
	            Mango--;
	            count++;
	            eaten=true;
	        }
	
	        else if(Apple!=0 && Mango!=0){
	            Apple--;
	            Mango--;
	            count++;
	            eaten=true;
	        }
	        
	        else {
	        	eaten=false;
	        	cout<<count<<endl;
	        }
        }
  }
  return 0;
}