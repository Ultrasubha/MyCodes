'''n,k = map(int,input().split(" "))
arr = list(map(int,input().split(" ")))
arr.insert(0,0)
print(, end ="")
'''
    
for _ in range(int(input())):
    n=int(input())
    arr = list(map(int,input().split(" ")))
    maxi = max(arr)
    for i in range(arr.count(maxi)):
        arr.remove(maxi)
    maxi1 = max(arr)
    print(maxi+maxi1)