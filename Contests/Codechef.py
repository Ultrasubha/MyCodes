'''n,k = map(int,input().split(" "))
arr = list(map(int,input().split(" ")))
arr.insert(0,0)
print(, end ="")
'''
def factorOf(n):         #T(n) = θ(√n)
    if n<2:
        return 1
    if n%2==0:
        return 2
    if n%3==0:
        return 3
    i=5
    while i*i<=n:
        if n%i==0:
            return i
        if n%(i+2)==0:
            return i+2
        i+=6
    else:
        return 0
    
for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(-1)
    elif n==2:
        print(1,1,1)
    else:
        found=False
        for i in range(1,n):
            c=n-i
            root=int(c**0.5)+1
            for j in range(2,root):
                if c%j==0:
                    found=True
                    print(j,n//j,i)
                    break
                else:
                    continue
            break
        if(found==False):
            print(-1)
            
        