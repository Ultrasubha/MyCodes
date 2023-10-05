x =  [1, 2, 2, 2, 3, 4, 4, 2, 2]
out = [1, [2, 3], 3, [4, 2], [2, 2]]

def exactDuplicateCounter(inp):
    arr=[]
    for i in set(inp):
        subarr=[0] * 2
        cnt = inp.count(i)
        subarr[0] = i
        subarr[1] = cnt
        arr.append(subarr)
    return arr

def plainDuplicateCounter(inp):
    arr=[]
    n = len(inp) - 1
    cnt=0
    for i in range(n):
        if inp[i] == inp[i+1]:
            cnt+=1
        else:
            if cnt > 0 :
                arr.append([inp[i], cnt+1])
            else:
                arr.append(inp[i])
            cnt=0
    if cnt > 0 :
        arr.append([inp[n], cnt+1])
    return arr

print(plainDuplicateCounter(x))
