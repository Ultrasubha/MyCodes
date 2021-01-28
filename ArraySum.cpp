//coded by Subhadeep Mandal
#include <iostream>
using namespace std;

int main() {
	int test_cases=1, size,i,j,arr[size],sum=0;
	
	cin >> test_cases;
	
	for(j=0;j<test_cases;j++)
	{
		cin >> size;
		for(i=0;i<size;i++)
		{
			cin >> arr[i];
		}
		
		for(i=0;i<size;i++)
		{
			sum+=arr[i];
		}
		
		cout << sum << endl;
		sum=0;
	}
	
	return 0;
}
