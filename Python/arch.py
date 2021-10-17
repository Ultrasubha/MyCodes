def unanswered(total,obtained):
	count=0
	for x in range(total,obtained,-1):
		count+=1
	return count

def wrongly_answered(total,obtained):
	count=0
	for x in range(total,int(obtained),-1):
		count+=1
	return count
	
print(wrongly_answered(30,25))

"""
Output
9 8 7 6 5 4 3 2 1 1 2 3 4 5 6 7 8 9 

9 8 7 6 5 4 3 2    2 3 4 5 6 7 8 9

9 8 7 6 5 4 3       3 4 5 6 7 8 9

9 8 7 6 5 4          4 5 6 7 8 9

9 8 7 6 5             5 6 7 8 9

9 8 7 6                6 7 8 9

9 8 7                   7 8 9

9 8                      8 9

9                         9
"""
