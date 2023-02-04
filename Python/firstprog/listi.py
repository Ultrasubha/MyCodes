grocery = ["Harpic", "Vimbar", "Lolipop", "Deodorant", "Bhindi"]
mixlizt = ["Harpic", "Vimbar", "Lolipop", "Deodorant", "Bhindi", "Dettol", 56]
# print(grocery[::-1])
# grocery.reverse()
# grocery.sort()
# print(max(grocery))
# print(min(grocery))
grocery.append("Alu")
grocery.insert(2, "Soap")
grocery.remove("Deodorant")
grocery.pop()  # Alu removed
print(grocery)

tp = (1, 2, 3)
tpl = (1,)
print(tpl)

a = 2
b = 8

a, b = b, a

print("a is", a, "and b is", b)

item1 = "Dettol"
item2 = "Lux_Soap"

if item1 in grocery:
    print(item1 + " is Listed")
elif item1 in mixlizt:
    print(item1 + " is Listed")
else:
    print("Not listed")

if item2 not in grocery:
    print(item2 + " is Not listed")
