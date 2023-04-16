'''n,k = map(int,input().split(" "))
arr = list(map(int,input().split(" ")))
arr.insert(0,0)
print(, end ="")
'''
def min_steps(n):
    # Count the number of bishops on each diagonal
    diag1 = diag2 = 0
    for i in range(1, n+1):
        if (i, i) in bishops:
            diag1 += 1
        if (i, n-i+1) in bishops:
            diag2 += 1
    
    # The minimum steps is the number of diagonals minus the number of bishops on those diagonals
    return n - diag1 + n - diag2
for _ in range(int(input())):
    n = int(input())
    if n<3:
        print(0)
    elif n<5:
        print(n-1)
    else: 
        print(n + (n-5)//2)
            
        