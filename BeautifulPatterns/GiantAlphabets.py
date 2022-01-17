#Created by Subhadeep Mandal
#Date: 24.11.2021
#Giant Alphabets
'''
OUTPUT
yes    yes
yes  yes
yesyes
yes  yes
yes    yes

    yesyes
  yes    yes
yes        yes
  yes    yes
    yesyes

yesyes     yes
yes yes    yes
yes  yes   yes
yes   yes  yes
yes    yes yes
'''

def N(size,content):
	str=""
	for i in range(size):
		str+=content+" "*i+content+" "*(size-i)+content+"\n"
	return str
		
def K(size,content):
	str=""
	for i in range(size):
		offset=abs((size//2)-i)
		str+=content+"  "*offset+content+"\n"
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

print(K(5,"yes"))	
print(O(5,"yes"))
print(N(5,"yes"))
