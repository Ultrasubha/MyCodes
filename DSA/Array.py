def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def reversedArray(arr):
    n=len(arr)
    for i in range(n//2):
        temp=arr[i]
        arr[i]=arr[n-1-i]
        arr[n-1-i]=temp
    return arr

#print(reversedArray([4,3,12,7,13]))
arr = [1,3,5]
arr.insert(1,45)
print(arr)