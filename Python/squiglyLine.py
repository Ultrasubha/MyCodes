'''
for n=15 To Print
15
14  7
13  8   6
12  9   5   2
11  10  4   3   1

[[2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]
'''

def arrSplitter(n,num):
    arr=[]
    start = 0
    end = 1
    incrementor = 1
    while end < n+1:
        arr.append(num[start:end])
        start = end
        incrementor +=1
        end += incrementor
    return arr

n = 15#int(input())
#print(num[:1],num[1:3],num[3:6],num[6:10],num[10:16])
num = arrSplitter(n, list(range(1, n+1)))
l = len(num)
print(num[-1:][0][-1:][0])
print(num[-1:][0][-2:-1][0], num[-2:-1][0][0])