n,m,y = map(int,input().split())
found=False
for x in range(m):
    if (x**n)%m==y:
        found=True
        print(x,end=" ")
if (found==False):
    print(-1)