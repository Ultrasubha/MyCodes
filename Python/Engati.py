#Questions Asked
#1) Reverse a string

def ReverseString(string):
    return string[::-1]

#2) palindrome - string

def isPalindrome(string):
    return string == ReverseString(string)

#3) Slice the string - too easy

#4) get current time (do it for IST too)
import datetime
newData = datetime.datetime(2023,12,25)
now = datetime.datetime.now()

#5) Print today's date and the date 2 days later
twoDaysLater = now + datetime.timedelta(days=2)
print(now, twoDaysLater)

#6) print prime numbers.
def isPrime(num):
    if num<2:
        return False
    if num<4:
        return True
    if num%2==0 or num%3==0:
        return False
    i=5
    while i*i<=num:
        if num%i==0 or num%(i+2)==0:
            return False
        i+=6
    return True

#7) Addition of two numbers using strings
def add(s1,s2):
    return eval(s1 + "+" + s2) 

#8) Syntax of linear search & binary search 
arr = [1, 3, 5, 6, 9, 12, 15, 18, 19]
#print("This is linear search", 5 in )
#9) Find largest number - too easy
#10) Find the value of 2X square + 5x+3=0 print it in quadratic equation
#11) Write code to print roots of quadratic equation
#12) count the number of vowels and consonants of any string.
vowels = lambda x: list(map(lambda c: c in "AEIOUaeiou", x)).count(True)
s = "Engati"
vowel = vowels(s)
print(vowel, len(s) - vowel)
    
#13) find the maximum length of the string. - too easy
#14) find largest array element. - too easy
#15) bubble sort
#16) n numbers are there and they should be multiple of 3 and after every number there must be "fin"
#17) Print 1 to N , every 5 multiple print Buzz
#18) collect phone numbers from many countries with country code and separate them from phone numbers. check if phone number is valid or not.
#19) enter mobile number of 10 digits should and it should start with 9 / 8 / 7 / 6 only in python
print(vowels("asd"))


