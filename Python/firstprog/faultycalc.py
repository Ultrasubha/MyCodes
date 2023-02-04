# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

user_input1 = int(input("Enter your first number: "))
user_input2 = int(input("Enter your second number: "))
user_input3 = (input("Enter your operator: +,-,*,/ "))

if user_input1 == 45 and user_input2 == 3 and user_input3 == '*':
    print("Your answer is: 555")

elif user_input1 == 56 and user_input2 == 6 and user_input3 == '/':
    print("Your answer is: 4")

elif user_input1 == 56 and user_input2 == 9 and user_input3 == '+':
    print("Your answer is: 77")

elif user_input3 == '+':
    print("Your answer is: ", user_input1 + user_input2)

elif user_input3 == '-':
    print("Your answer is: ", user_input1 - user_input2)

elif user_input3 == '*':
    print("Your answer is: ", user_input1 * user_input2)

elif user_input3 == '/':
    print("Your answer is: ", user_input1 / user_input2)
else:
    print("Invalid input try again!!")
