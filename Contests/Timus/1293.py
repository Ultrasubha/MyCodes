# https://acm.timus.ru/problem.aspx?space=1&num=1293
arr=list(map(int,input().split()))
val=2
for i in arr:
    val*=i
print(val)