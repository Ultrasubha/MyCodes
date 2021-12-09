'''
Caesar Cipher (with Python)
Crested by Subhadeep Mandal
 
LICENSING:
  GNU General Public License v3.0  .....Dated: 8-12-2021
  (c) 2021 Guava_Slice. All rights reserved.
'''
lst = [ord(i) for i in input("Enter your sentence\n")]
offset =  int(input("shift amount :"))
msg="\n"
for i in lst:
	if i==32:
		msg+=" "
	elif i>=64 and i<=90:
		msg+= chr((i + offset -65) % 26 + 65)
	elif i>=97 and i<=122:
		msg+= chr((i + offset - 97) % 26 + 97)
	else:
		msg = "\nPlease enter only alphanumeric characters"
		break
print(msg)
