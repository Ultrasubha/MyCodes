/*
Given an array Numbers[] and a number N, display for all pair in Numbers[] with difference
as 2N
Test Case 1
Inputs:
Numbers[] = { 3, 1, 1 }
N = 1
Output: (3,1)
Test Case 2
Inputs:
Numbers[] = { 16, 4, 10, 6, 1, -8 }
N = 3
Output: (16, 10), (4, 10)

Coded by Subhadeep Mandal
Date:28.11.2021
Question Source : https://github.com/prakartigoel24/Coding-Round-Questions/blob/main/Hexaview%20Technologies/
*/

#include <iostream>
using namespace std;

int main() {
	int arr_size = 0, N = 0;
	
	//input for array size
	cin>>arr_size;
	
	//input for the N of the difference
	cin>>N;
	int Numbers[arr_size];
	
	//Filling up the array with input data
	for(int i=0;i<arr_size;i++)
		cin>>Numbers[i];
	
	/*With a double loop it's being checked if 1st element in array
	and the difference of any other element gives the result of 2N
	
	In other words for each I all the values of J will be checked
	
	Hence Complexity = O(arr_size*arr_size)
	*/
	for(int i=0;i<arr_size;i++){
		for(int j=0;j<arr_size;j++)
			if(Numbers[i]-Numbers[j]==2*N)
				cout << "(" << Numbers[i] << "," << Numbers[j] << ")";
	}
		
	return 0;
}
