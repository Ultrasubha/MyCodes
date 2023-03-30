'''n,k = map(int,input().split(" "))
arr = list(map(int,input().split(" ")))
arr.insert(0,0)
print(, end ="")
'''
    
for _ in range(int(input())):
    n,p,q = map(int,input().split(" "))
    s = input()
    s1=""
    for i in range(n):
        val = ord(s[i])
        if p==0 and q==0:
            s1+=s[i]
        else:
            if val + p > 122:
                s1+="a"
                p -= (123 - val)
            elif q>0:
                if val - q < 97:
                    s1+="a"
                    q -= (val - 97)
                else:
                    s1+=chr(val - q)
                    q=0
            else:
                s1+=s[i]
    print(s1)
        