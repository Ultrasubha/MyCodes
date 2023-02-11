for _ in range(int(input())):
    s = input()
    n = s[1:]
    s = ord(s[:1]) - 96
    if n>4:
        n = 9-n
    
    if n==1 or s==1:
        print(2)
    elif n==2 or s==2:
        print(3)
    elif n==3 or s==3:
        print(4)