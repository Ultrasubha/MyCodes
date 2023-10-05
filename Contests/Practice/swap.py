def bitSwap(a,b):
    a^=b
    b^=a
    a^=b
    return a, b
    
def pythonSwap(a,b):
    return b, a

def plainSwap(a,b):
    b -= a
    a += b
    b = a - b
    return a,b
print(plainSwap(2,5))