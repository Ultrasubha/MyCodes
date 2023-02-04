#include <iostream>
using namespace std;
 
 int count=0;
void towerOfHanoi(int n, char source, char destination, char Aux)
{
    if (n == 1)
    {
        count++;
        cout << "Move disk 1 from rod " << source <<" to rod " << destination<<endl;
        return;
    }

    towerOfHanoi(n - 1, source, Aux, destination);
    count++;
    cout << "Move disk " << n << " from rod " << source <<" to rod " << destination << endl;
    towerOfHanoi(n - 1, Aux, destination, source);
}
 
int main()
{
    int n = 5;
    towerOfHanoi(n, 's', 'a', 'd');
    cout << "Total steps :" << count <<endl;
    return 0;
}