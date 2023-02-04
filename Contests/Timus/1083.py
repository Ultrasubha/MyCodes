n,k=input().split()
val=1
n=int(n)
k=k.count("!")
while n>1:
    val*=n
    n-=k
print(val)