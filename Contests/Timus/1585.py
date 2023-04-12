e,m,l=0,0,0
for i in range(int(input())):
    s=input()
    if s=="Emperor Penguin":
        e+=1
    elif s=="Macaroni Penguin":
        m+=1
    else:
        l+=1
maxi = max(e,m,l)
if maxi==e:
    print("Emperor Penguin")
elif maxi==m:
    print("Macaroni Penguin")
else:
    print("Little Penguin")