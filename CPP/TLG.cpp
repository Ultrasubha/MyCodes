#include <iostream>
using namespace std;

int main() {
	int T, x, y, p1Score = 0, p2Score = 0, lead=0,winner;
	cin >> T;
	for(int i=0;i<T;i++) {
        cin>>x>>y;
        p1Score+=x;
        p2Score+=y;

        if(p1Score>p2Score){
            if(lead<(p1Score - p2Score)){
                lead = p1Score - p2Score;
                winner = 1;
            }
        }
        else{
            if(lead<(p2Score - p1Score)){
                lead = p2Score - p1Score;
                winner = 2;
            }
        }
    }

    cout<<winner<<" "<<lead<<endl;
	return 0;
}