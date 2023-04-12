#include<bits/stdc++.h>
using namespace std;

int length(int num){
    int cnt=0;
    while(num>0){
        num/=10;
        cnt++;
    }
    return cnt;
}

int solution(int N) {
    int num = N,rem=0, case1=0, case2=0;
    while(num>0){
        rem=num%10;
        num/=10;
        if(rem==5) {case1=num; break;}
    }

    string s = to_string(num);
    for(int i=0;i<s.length() -1;i++){
        if(s[i]=='5') s[i]=s[i+1];
    }
    case2 = atoi(s);
    return std::max(case1,case2);
}

int main(){
    //int x=59145;
    /*int num=x;
    while(num>0){
        num%=10;
        cout<<num<< " ";
    }*/
    //cout<<solution(x)<<endl;
}