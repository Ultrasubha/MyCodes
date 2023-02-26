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

'''for _ in range(int(input())):
    a,b,c = map(int,input().split(" "))
    a=a-min(a,b)
    a=a-abs(min(a,c))
    if a<0:
        print(a,"NO")
    else:
        print(a,"YES")'''
for _ in range(int(input())):
    n,k = map(int,input().split(" "))
    problemTime = list(map(int,input().split(" ")))
    breakTime = list(map(int,input().split(" ")))
    TotalTime=[]
    for i in range(n):
        TotalTime.append(problemTime[i] + breakTime[i])
    #name_mark_pairs = list(zip(problemTime, breakTime))
    print(TotalTime)
#sorted_pairs = sorted(name_mark_pairs, key=lambda x: x[0])
#for i in sorted_pairs:
#    print(i[1])