#Created by Subhadeep Mandal
#Date: January 6,2022
import random 
lst = [chr(i) for i in range(33,127)]

len = int(input("How long do you want your password?\n"))

print("".join(random.sample(lst,len)))
