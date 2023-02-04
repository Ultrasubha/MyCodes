# https://acm.timus.ru/problem.aspx?space=1&num=1002

arr=[2,2,2,3,3,3,4,4,1,1,5,5,6,6,0,7,0,7,7,8,8,8,9,9,9,0]
s=input()
N=int(input())
arr=["."]*N
for i in range(N):
    arr[i]=input()
for i in range(97,123):
	print(chr(i),arr[i-97])