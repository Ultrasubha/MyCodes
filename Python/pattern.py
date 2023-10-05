n = 3
num = 1
for i in range(1, n + 1):
    for j in range(n - i):
        print("_", end="")
    for j in range(2 * i - 1):
        print(num, end="")
        num += 1
    for j in range(n - i):
        print("_", end="")
    print()