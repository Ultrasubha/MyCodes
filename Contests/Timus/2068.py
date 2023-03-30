n = int(input())
arr = list(map(int,input().split()))
cnt=0
for i in arr:
    cnt+=i//2
if cnt%2:
    print("Daenerys")
else:
    print("Stannis")