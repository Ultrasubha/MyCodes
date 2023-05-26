def log2(num):
    cnt=0
    while num>0:
        num>>=1
        cnt+=1
    return cnt-1
        

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def swappNumbers(a,b):
    a^=b
    b^=a
    a^=b
    return a,b

def firstSetBit(n):
    if n==0:
        return 0
    return n&(-n)

def firstSetBitPosition(n):
    return int(log2(firstSetBit(n)))

def countSetBits(n):
    cnt=0
    while n>0:
        n&=(n-1)
        cnt+=1
    return cnt

def flippedNumber(num):
    k=1
    while k<num:
        k<<=1
    return k-1-num
        
print(log2(10))