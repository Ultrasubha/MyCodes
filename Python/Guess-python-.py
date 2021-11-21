import random
numberofattempts=0
print("Hello! What is your name?")
myname=input()
number=random.randint(1,20)
print('Well,'+myname+',I am thinking of a number between 1 and 20.')
while numberofattempts<6:
    print('take a guess')
    guess=input()
    guess=int(guess)
    numberofattempts+=1
    if guess<number:
        print('your guess is low')
    if guess>number:
        print('your guess is too high')
    if guess==number:
        break
if guess==number:
    numberofattempts=str(numberofattempts)
    print('Good Job,'+myname+'! You guessed my number in'+numberofattempts+' Guesses !')
if guess !=number:
    number=str(number)
    print('Nope. The number I was thinking of was '+number)
