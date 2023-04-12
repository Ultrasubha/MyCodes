import math
def bruteForce(n):
    s=""
    for i in range(1,n+1):
        s+=str(i)
        if i!=n:
            if i%2:
                s+="+"
            else:
                s+="-"
    if eval(s)%2:
        return "grimy"
    else:
        return "black"
    
def smartApproach(n):
    if math.ceil(n / 2) % 2:
        return "grimy"
    else:
        return "black"
    
print(smartApproach(int(input())))