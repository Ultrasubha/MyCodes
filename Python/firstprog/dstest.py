def max3bad(x,y,z):
  maximum = 0
  if x >= y:
    if x >= z:
      maximum = x
  elif y >= z:
    maximum = y
  else:
    maximum = z
  return(maximum)

x, y, z = input("Enter a three value: ").split()

print(max3bad(x,y,z))