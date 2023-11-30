def add(lt):
    z=0
    for i in lt:
        z += i
    return z

def squaresum(n):
    sm=0
    cnt=1
    while cnt<5:
    #for i in range(1,n+1):
        sm+=cnt*cnt
        cnt+=1
    return sm
    #if sm>10:
    #    return 45
    #else:
    #    return 23