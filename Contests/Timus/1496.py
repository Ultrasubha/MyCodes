lst=[]
duplicate=[]
for _ in range(int(input())):
    s=input()
    if s not in duplicate:    
        if s in lst:
            duplicate.append(s)
        else:
            lst.append(s)
for i in duplicate:
    print(i)
    
