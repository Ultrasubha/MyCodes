def purified(s):
    i=0
    s1=""
    while i<(len(s)-1):
        if s[i]==s[i+1]:
            i+=2
        else:
            s1+=s[i]
            i+=1
    s1+=s[i]
    for i in range(len(s1)-1):
        if s1[i]==s1[i+1]:
            return purified(s1)
    return s1
s="wwstdaadierfflitzzz"
print(purified(s))