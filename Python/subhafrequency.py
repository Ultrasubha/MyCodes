def cnt(s,c):
    ct=0
    for i in s:
        if i==c:
            ct+=1
    return ct
s = "subhadeepmandal"
unique = set(s)
for i in unique:
    print(i,cnt(s,i))