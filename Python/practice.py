#Simple Password Generator, Coded by Subhadeep Mandal.As per IBM password policy [Uppercase] + [Lowercase] + [numerals] + [special characters]
import random
characters = lambda x,y: [chr(i) for i in range(x,y)]
lst = characters(65,91) + characters(97,123) + characters(48,58) + ["!", "@", "#", "$", "%", "^", "&", "*"]
print("Your password : ","".join(random.sample(lst,int(input("Password Length? : ")))))