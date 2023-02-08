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
    arr = list(map(int,input().split(" ")))
    cost= arr[len(arr)-1]
    arr.pop()
    add=max(arr)
    arr.remove(add)
    add+=max(arr)
    if add>=cost:
        print("YES")
    else:
        print("NO")