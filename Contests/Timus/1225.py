n=int(input())+1
arr=[0]*n
for i in range(n):
    if i==1 or i==2:
        arr[i] = 2
    else:
        arr[i] = arr[i-1] + arr[i-2]
print(arr[n-1])
