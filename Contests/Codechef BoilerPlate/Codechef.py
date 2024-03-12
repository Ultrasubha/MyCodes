'''n,k = map(int,input().split(" "))
arr = list(map(int,input().split(" ")))
arr.insert(0,0)
print(, end ="")

1
6
1 7 3 0 2 13
0 2 3 4 5 0
'''

def cnt(Arr):
    maxi=0
    for i in Arr:
        arr=i.split(" ")
        n = len(arr)
        if arr[-1]=="0":
            n-=1
        if arr[0]=="0":
            n-=1
        lst.append(arr)
    return lst

for _ in range(int(input())):
    n = int(input())
    om = input().split(" 0 ")
    addy = input().split(" 0 ")
    print(cnt(om))
    print(cnt(addy))
    
