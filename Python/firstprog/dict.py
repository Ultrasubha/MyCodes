d1 = {"Harry": "coder", "Subhadeep": "Gamedeveloper", "Ribhu": "Animator", "Chasa": "Hacker"}
d1["Jyoti"] = "Civil_Engineer"
d1[520] = "Something"
d1["Shobhon"] = {"First": "coder", "Second": "Animator", "Third": "Java Developer"}
d2 = d1.copy()
del d1[520]
# print(d1["Shobhon"]["Second"])

print(d1.get("Harry"))
print(d1["Harry"])

d2.update({"Leena": "Software_Developer"})

print(d2)
print("\nThe keys of d2 are", d2.keys())
print("\nThe items of d2 are", d2.items())
