'''
MyClass chat Filter
Coded by Subhadeep Mandal
On Ideone -> https://i...content-available-to-author-only...e.com/c4LC7s
Dated 
26-1-2022
'''
from sys import stdin 
useless = ["Good","good","gud","Afternoon","afternoon","Morning","morning","yes","ys","s","Yes",
"clear","Clear","Ok","ok","Okay","Ma'am","Understood","understood","Sir","sir","mam","ma'am","got it",
"thnx","ig"]
#Poll answer filter to be done later for "A","B","C","D","a","b","c","d"
 
lines = stdin.read().splitlines()	#Array of lines
for line in lines:
	if line[len(line)-1] == "%":	#To weed off poll results
		continue
	line = line.split(":")[2]		#Core message
	lst = line.split(" ")			#Each word of Core msg
	if any(item in lst for item in useless):	#Discarding useless line
		continue
	else:
		print(line)
