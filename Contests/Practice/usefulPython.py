x = [chr(i) for i in range(97,105)] #small Letters
y = list(map(lambda y: chr(ord(y) - 32),x)) #caps
z = list(map(lambda a,b:a+b, x,y)) #both

zipped = list(zip(x,y))
for i in enumerate(zipped):
    print(i)