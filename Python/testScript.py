#Code Snippets------------------------------
#print(i, end =" ")
#a,b = map(int,input().split(" "))
#arr = input().split(" ")
#' '.join(map(str, result))
'''
N = int(input())
arr = list(map(int,input().split(" ")))
for i in range(N):
	arr[i]
'''
def euclideanGCD(x,y):
	while y:
		x,y = y, x%y
	return x
'''
s = ""
l=["a","b","c","d"]
print("".join(l))
'''
def checkOne(a,b):
    val = 0
    c1 = bin(a).replace("0b", "").count('1')
    c2 = bin(b).replace("0b", "").count('1')
    
    if max(c1,c2)==c2:
        val=b
    elif max(c1,c2)==c1:
        val=a
    return val

n=int(input())
if n==6:
    exit()
else:
    a=int(input())
    b=int(input())
    if n==1:
        val=a+b
    elif n==2:
        val=a-b
    elif n==3:
        val=a*b
    elif n==4:
        val=a/b
    elif n==5:
        val=a%b
    print(val)