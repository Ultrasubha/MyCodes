s=input()
d=int(input())
s1=""
for i in range(len(s)-1):
    if ord(s[i])>=97 and ord(s[i])<=122:
        s1+=chr(((ord(s[i])-97 + d)%26)+97)
    else:
        s1+=s[i]
print(s1)