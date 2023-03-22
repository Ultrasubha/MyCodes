class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return "I am a person"
    
p1 = Person("Subhadeep", 27)
print(p1.name, p1.age)
print(p1)