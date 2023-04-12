'''n,k = map(int,input().split(" "))
arr = list(map(int,input().split(" ")))
arr.insert(0,0)
print(, end ="")
'''

for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int,input().split(" "))))
    print("arr[n-2] = ",arr[n-2])
    if n==2:
        print("NO")
    else:
        if arr[0]==arr[n-2]:
            print("NO")
        else:
            print("YES")