lst=[]
for i in range(int(input())):
    lst.append(input())
c=input()
for i in lst:
    if i[0]==c:
        print(i)