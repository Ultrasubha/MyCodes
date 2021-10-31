/*PrepByte Competition
Dev has three baskets of fruits:
The first basket contains only apples, and there are A apples in it.
The second basket contains only bananas, and there are B bananas in it.
The third basket contains only mangoes, and there are M mangoes in it. 
Each day Dev eats exactly two different fruits. He can't eat two same fruits in a day. 
For example, he can eat one apple and one mango in a single day, but he cannot eat two apples in a single day.
Your task is to find the maximal number of days Dev can eat fruits.

The first line of the input contains an integer T denoting the number of test cases.
Then T test cases follow:
Each test case contains three integers A,B and M denoting the number of apples, bananas and mangoes respectively.

Input:
6
1 1 1
1 2 1
4 1 1
8 5 11
6 2 7
5 7 6
Output:
1
2
2
8
6
7
Expected Output:
1
2
2
12
7
9
*/
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
