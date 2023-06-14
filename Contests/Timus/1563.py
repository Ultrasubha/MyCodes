arr={0}
arr.remove(0)
cnt=0
for i in range(int(input())):
    val=input()
    if val in arr:
        cnt+=1
    else:
        arr.add(val)
print(cnt)