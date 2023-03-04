N=int(input())
cnt=N+2
for i in range(N):
    if "+" in input():
        cnt+=1
if cnt==13:
    cnt+=1
print(cnt*100)