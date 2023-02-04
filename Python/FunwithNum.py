'''
On the occassion of National Mathematics Day in memory of the 
great mathematician Srinivasa Ramanujan. I created this code

Date : December 22,2021
Created by Subhadeep Mandal

Output = [1729, 4104, 13832] are Ramanujan Numbers
'''

#uptoNum is max limit of a,b,c,d whose cubes will be tested
uptoNum = 25
RamNum = []
for a in range(uptoNum):
	for b in range(uptoNum):
		for c in range(uptoNum):
			for d in range(uptoNum):
				if a != b and a != c and a != d and b != c and b != d and c != d:
                                    if (a**3+b**3==c**3+d**3):
				                                    RamNum.append(a**3+b**3)
RamNum = sorted(set(RamNum))											
print(RamNum, "are Ramanujan Numbers")