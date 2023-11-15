#Use verify [file] to test your solution and see how it does.
#When you are finished editing your code, use submit [file] to submit your answer.
#If your solution passes the test cases, it will be removed from your home folder.

def solve(arr,num):
    rt = int(num**0.5)
    sq = rt*rt
    arr.append(sq)
    if num>1:
        return solve(arr,num-sq)
    else:
        if arr[-1]==0:
            arr.pop()
        return arr #",".join(map(str,arr))
        
def solution(area):
    arr = []
    return solve(arr,area)

print(solution(4))