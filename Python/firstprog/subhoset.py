s1 = set()
print(type(s1))
prime = set([2, 3, 5, 7, 11, 13, 17, 19])
random = set([4, 8, 9, 10, 12, 142, 3, 5, 7])
prime.add(23)
prime.add(29)
prime.add(5)
print("The union of both sets is " + str(prime.union(random)))
print("The intersection of both sets is " + str(prime.intersection(random)))
print("Number of elements in prime = " + str(len(prime)))
# similarly min,max,disjoint can be found. Search internet for more