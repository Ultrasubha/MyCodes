#Q.1)Given nums = [1,2,3,4] make an array of its products [24,12,8,6] without using the division operator.

nums = [7,5,3,6]
out=[]
n=len(nums)
for i in range(n):
    for j in range(n):#i=1 and j=3
        if i!=j:
            val = nums[i]*nums[j]#2*3
            if val not in out and val not in nums:
                out.append(val)
val=1
for k in range(n):
    val=val*nums[k]
out.append(val)
print(out)
#Q.2)given an array=[1,2,3,4] target=7. 
# Return an array of length 2 which will represent the indices
#such that if i sum 2 indices target comes
arr=[1,2,3,4]
target=7
sum=0
indices=[]
for i in reversed(range(len(arr))):
    if arr[i]+sum<= target:
        sum+=arr[i]
        indices.append(i)
    if sum==target:
        break
print(indices)
        