def N(size,content):
	str=""
	for i in range(size):
		str+=content+" "*i+content+" "*(size-i)+content+"\n"
	return str
	
def O(size,content):
	str=""
	str1=""
	for i in range(size):
		ext_offset=(size//2)-i
			
		if ext_offset<0:
			int_offset-=2
		else:
			int_offset=i+i
			
		str+="  "*abs(ext_offset) + content + "  "*int_offset + content
		
		if size%2==0:
			if i==0:
				str1=str
		str+="\n"
	str+=str1
	return str
	
lst1 = N(6,"yes").split("\n")
lst2 = O(6,"yes").split("\n")
lst3=""

for i in range(6):
	lst3 += lst1[i]+"  "+lst2[i]+"\n"
	
var=input("You wanted to ask something?\n")
if var=="Is Schrödinger's cat alive?":
	print(lst3)
else:
	print("You are only allowed to ask 1 question that is,")
	print("Is Schrödinger's cat alive?")
