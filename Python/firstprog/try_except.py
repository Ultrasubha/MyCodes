print("Enter num1")
a = input()
print("Enter num2")
b = input()
try:
    print("The sum of the 2 integers is :", int(a) + int(b))
except Exception as v:
    print(v)

print("Code ended")
