model = "I have been waiting for you sir"
model1 = "Better_Late_Than_never"
model2 = "subho"
length = len(model)
# print(model[::-1]) #to reverse
# print(model[7:-12]) #been waiting
# print(model[7:19]) #been waiting
# print(model2.isalnum())
# print(model.endswith("sir"))
# print(model.count("i"))
# print(model2.capitalize()) works on 1st letter only
# print(model.find("i"))
# print(model.upper())
# print(model.lower())
# print(model.replace("have been", "was"))
print(model.replace(model[2:11], "was"))  # same thing as above
