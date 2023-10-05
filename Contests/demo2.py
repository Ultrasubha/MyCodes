#print today + next 2 days
s= "06-09-2023"
arr=s.split("-")
s1 = str(int(arr[0]) + 2) + "-" +arr[1] + "-" + arr[2]
print(s, s1)