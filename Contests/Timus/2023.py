def box(name):
    c=name[:1]
    b1="PORA"
    b2="BMS"
    if c in b1:
        return 0
    elif c in b2:
        return 1
    else:
        return 2
steps=0
prev=0
for i in range(int(input())):
    curr=box(input())
    steps+=abs(prev-curr)
    prev = curr
print(steps)