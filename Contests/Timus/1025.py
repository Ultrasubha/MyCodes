K=int(input())//2+1
arr=sorted(list(map(int,input().split())))
val=0
for i in range(K):
    val+=arr[i]//2+1
print(val)