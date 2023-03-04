k,n=map(int,input().split())
arr = list(map(int,input().split()))
rem=0
for i in arr:
    if (rem+i)>k:
        rem+=(i-k)
    else:
        rem=0
print(rem)