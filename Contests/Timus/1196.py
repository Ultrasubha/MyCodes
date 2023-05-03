profDates={0}
profDates.clear()
for i in range(int(input())):
    profDates.add(int(input()))
cnt=0
for j in range(int(input())):
    if int(input()) in profDates:
        cnt+=1
print(cnt)