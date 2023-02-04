# https://acm.timus.ru/problem.aspx?space=1&num=1005
N=int(input())
arr=list(map(int,input().split()))
pile1=0
pile2=0
while len(arr)>0:
    M=max(arr)
    if pile1>pile2:
        pile2+=M
    else:
        pile1+=M
    arr.remove(M)
print(abs(pile1-pile2))

