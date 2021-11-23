'''
EASILY PERFORM LIST OPERATIONS FROM INPUT COMMANDS


INPUT:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

OUTPUT:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''
N = int(input())
arr=[]

for i in range(N):
	Demand = input().split()
	if Demand[0]=="print":
		print(arr)
	elif Demand[0]=="insert":
		arr.insert(Demand[1],Demand[2])
	elif Demand[0]=="remove":
		arr.remove(Demand[1])
	elif Demand[0]=="append":
		arr.append(Demand[1])
	elif Demand[0]=="pop":
		arr.pop(Demand[1])
	elif Demand[0]=="sort":
		arr.sort()
	else:
		arr.reverse()
