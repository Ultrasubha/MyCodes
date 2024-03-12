import os

def yesterday():
    file = "yesterday.txt"
    if os.path.exists(file):
        with open(file, "r") as file:
            content = file.read()
        return content
    else:
        content = input("What did you work on yesterday?\n")
        with open(file, "w") as file:
            file.write(content)
        return content
    
print(yesterday())