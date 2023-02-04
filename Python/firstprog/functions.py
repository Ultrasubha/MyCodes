a = 9
b = 5
c = sum((a, b))
print(c)


def speed(Distance, Time):
    """Calculates speed from Distance and Time"""
    return Distance / Time


def random():
    print("Let's see")


print("The speed is" + str(speed(12, 6)))
print(speed.__doc__)
