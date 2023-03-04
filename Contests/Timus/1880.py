a=input()
a1=list(map(int,input().split()))
b=input()
b1=list(map(int,input().split()))
c=input()
c1=list(map(int,input().split()))
cnt=0
for i in a1:
    if i in b1:
        if i in c1:
            cnt+=1
print(cnt)