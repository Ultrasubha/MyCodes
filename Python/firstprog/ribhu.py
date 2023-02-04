num = 18
while True:
    value = int(input("Guess the number :"))
    if value == num:
        print("You have guessed the number\n")
        break
    elif (value > num):
        print("Try Decreasing\n")
        continue
    elif (value < num):
        print("Try Increasing\n")
        continue
