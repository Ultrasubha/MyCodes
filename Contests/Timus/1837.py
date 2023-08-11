'''one=[]
two=[]
three=[]
for i in range(int(input())):
    arr = input().split(' ')
    if "Isenbaev" in arr:
        for j in arr:
            if j!="Isenbaev":
                one.append(j)
    for j in arr:
        if j in one:
            two.append(j)
    for j in arr:
        if j in two:
            three.append(j)
    '''
#print("bi" in "abig")
members = ["isenbaev 0"]
for i in range(int(input())):
    arr = input().split(' ')
    membar = list(map(lambda s:s[:-2],members))
    if "Isenbaev" in arr:
        for j in arr:
            if j!="Isenbaev" and j not in membar:
                members.append(j + " 1")
                arr=[]
    for k in arr:
        if k in membar:
            #members.append(k +
print(members)