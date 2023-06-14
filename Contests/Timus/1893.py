seat=input()
numeric, alphabet = int(seat[:-1]),seat[-1:]
#print(numeric, alphabet)
if numeric<3:
    if alphabet in "BC":
        print("aisle")
    else:
        print("window")
elif numeric<21:
    if alphabet in "BCDE":
        print("aisle")
    else:
        print("window")
else:
    if alphabet in "CDGH":
        print("aisle")
    elif alphabet in "AK":
        print("window")
    else:
        print("neither")