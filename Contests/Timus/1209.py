def is_in_series(x):
    n = (-1 + (1 + 8 * (x - 1)) ** 0.5) / 2
    return 1 if n.is_integer() else 0

for i in range(int(input())):
    print(is_in_series(int(input())), end=" ")
print()