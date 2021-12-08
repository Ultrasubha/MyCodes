'''
Caesar Cipher (with Python)
Crested by Subhadeep Mandal
 
LICENSING:
  GNU General Public License v3.0  .....Dated: 8-12-2021
  (c) 2021 Guava_Slice. All rights reserved.
'''

lst = [ord(i) for i in input("Enter your sentence\n")]
 
offset =  int(input("shift amount :"))
lst = list(map(lambda x: x+offset if(x != 32) else 0, lst))
for i in range(len(lst)):
	if lst[i]>122:
		lst[i] = 96 + (lst[i]-122)
	elif lst[i]<65:
		lst[i] = 91 - (65-lst[i])

str="\n"
for i in range(len(lst)):
	if lst[i] != 0:
		str+=chr(lst[i])
	else:
		str+=" "
print(str)
