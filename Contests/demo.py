'''lst=["my day was horrible","I am sad","I don't feel very well","I am disappointed"]
nlst=[]
for i in lst:
    for j in i.split(" "):
        nlst.append(j)
unik=set(nlst)
for i in unik:
    print(i,nlst.count(i))'''

