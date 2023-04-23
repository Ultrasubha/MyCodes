'''n,k = map(int,input().split(" "))
arr = list(map(int,input().split(" ")))
arr.insert(0,0)
print(, end ="")
'''
for _ in range(int(input())):
    n,x = map(int,input().split(" "))
    arr = list(map(int,input().split(" ")))
    ans=0
    for i in range(30):
        m=0
        for j in range(n):
            m|=1<<(arr[j]>>i)&1
        if m!=3:
            continue
        t=x
        if t & (1<<i):
            t^=1<<i
            for j in reversed(range(0,i)):
                t|=1<<j
    print(max(ans,t))
            
        