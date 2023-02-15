'''n,k = map(int,input().split(" "))
arr = list(map(int,input().split(" ")))
arr.insert(0,0)
print(, end ="")
'''

'''import sys
from turtle import clear
sys.stdin = open('CP1/sampleinput1.txt' ,'r')
sys.stdout= open('CP1/myoutput1.txt','W')
'''

for _ in range(int(input())):
    a,b,c = map(int,input().split(" "))
    a=a-min(a,b)
    a=a-abs(min(a,c))
    if a<0:
        print(a,"NO")
    else:
        print(a,"YES")