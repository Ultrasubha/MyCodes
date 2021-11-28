'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

INPUT:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

OUTPUT:
Berry
Harry
'''

d={} #Empty dictionary
for _ in range(int(raw_input())): #Range for number of students
    Name=raw_input() #Accepting name of the student
    Grade=float(raw_input()) #Accepting the grade of the student
    d[Name]=Grade #Assigning name as key and grade as value for the dictionary
v=d.values()#Obtaining the values of dictionary(all grades of students)
second=sorted(list(set(v)))[1] #Removing duplicte grades by using set data type , changing it to list, sorting in ascending order and taking the second lowest grade
second_lowest=[] #Declaring an empty list for storing the name of the students who got the second lowest grade
for key,value in d.items():  #Going through the name and grade of each students by using items() method of dictionary
    if value==second: #Checking whether the grade is equal to the second lowest grade
        second_lowest.append(key) #If yes , append it to the second_lowest list
second_lowest.sort() #Sorting the name of students in asceding order
for name in second_lowest: #Going through the name of each students who got the second lowest grade
    print name #Printing each name of students in seperate line
    
