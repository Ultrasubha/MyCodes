#Simple Password Generator, Coded by Subhadeep Mandal.As per IBM password policy [Uppercase] + [Lowercase] + [numerals] + [special characters]
'''import random
characters = lambda x,y: [chr(i) for i in range(x,y)]
lst = characters(65,91) + characters(97,123) + characters(48,58) + ["!", "@", "#", "$", "%", "^", "&", "*"]
print("Your password : ","".join(random.sample(lst,int(input("Password Length? : ")))))'''
def answer(area):
    res = []
    while (area > 0):
        biggest_square_side = int(area ** 0.5)
        biggest_square = biggest_square_side ** 2
        area -= biggest_square
        res.append(biggest_square)
    return res

def solve(arr,num):
    rt = int(num**0.5)
    sq = rt*rt
    arr.append(sq)
    if num>1:
        return solve(arr,num-sq)
    else:
        if arr[-1]==0:
            arr.pop()
        return arr
        
def solution(area):
    arr = []
    return solve(arr,area)

for i in range(1,1000000):
    if answer(i)!=solution(i):
        print(i,answer(i),solution(i))