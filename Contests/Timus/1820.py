n,k=map(int,input().split())
val=2*n
if n>k:
    if val%k:
        val=val//k + 1
    else:
        val=val//k
else:
    val=2
print(val)
        