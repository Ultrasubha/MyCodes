#include<bits/stdc++.h>
using namespace std;

int main(){
    string s; getline(cin, s);
    int taps=0;
    for(char v:s) {
        if(v==' ' || v=='_' || v=='.') taps++;
        else if (v=='!') taps+=3;
        else{
            if (!(v%3)) taps+=3;
            else taps+=v%3;
        }
    }
    cout<<taps<<endl;
    return 0;
}