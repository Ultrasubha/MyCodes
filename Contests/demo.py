'''#   0, 4, 22, 4, 14, 4, 2
#   0, 1, 2, 4, 1, 1, 1
def waveSorting(arr):
    arr.sort()
    for i in range(1, len(arr), 2):
        if arr[i-1] < arr[i]:
            return "false"
    for i in range(2, len(arr), 2):
        if arr[i-1] > arr[i]:
            return "false"
    return "true"



print(waveSorting([0, 1, 2, 4, 1, 1, 1]))
print(waveSorting([0, 4, 22, 4, 14, 4, 2]))'''
#for i in range(97, 123):
#   print(chr(i),i)
a = [2,4,23,2,5,7]
print(list(map(lambda x: x.replace(2, "_"), a)))