N=int(input())
val=0
if N>0:
    for i in range(N+1):
        val += i
else:
    i=1
    while i>=N:
        val+=i
        i-=1
print(val)