s=input()
if len(s)!=(16 or 19):
    print("Invalid")
else:
    for i in range(16):
        num = ord(s[i])
        if (num==45 and s[i]%4==0) or (num>47 and num<58):
            print("Valid")
            break 
        else:
            print("Invalid")
            break