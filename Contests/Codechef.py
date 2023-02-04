'''n,k = map(int,input().split(" "))
arr = list(map(int,input().split(" ")))
arr.insert(0,0)
j = 1
i = 1
ans = 0
print(, end ="")
'''

'''import sys
from turtle import clear
sys.stdin = open('CP1/sampleinput1.txt' ,'r')
sys.stdout= open('CP1/myoutput1.txt','W')
'''

def gcd(a, b):
    if a == 0 :
        return b

    return gcd(b%a, a)

for _ in range(int(input())):
    N=int(input())
    s=input()
    for i in s:
        val=26-ord(s[i])-96