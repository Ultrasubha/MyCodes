'''
Agenda
1) File Handling
2) Regex
3) Date Time
4) OS
5) map, lambda expression
6) Dictionary
7) 
8) 
9) 
10) 
11) 
12) 
13) 
14)
15)
16)
17)
18)
19)
'''

file = open("D:\_WorkSpace\MyCodes\Python\practiceText.txt", "w")
s = "Hi, this is me, Subhadeep.\nA Simple guy with simple dreams.\nWanting to develop games for all to play and enjoy.\nIf you ever comes accross a guy wanting to be a game developer in Japan, rest assured you just met Subhadeep"
file.write(s)
file.close()
import re
print(re.findall("^H.*", s))