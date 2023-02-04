# https://acm.timus.ru/problem.aspx?space=1&num=1001
import math

def square_root(n):
    return format(math.sqrt(n), '.4f')

numbers = []
while True:
    try:
        line = input().strip()
        if line:
            for number in line.split():
                numbers.append(int(number))
    except EOFError:
        break

for n in numbers[::-1]:
    print(square_root(n))