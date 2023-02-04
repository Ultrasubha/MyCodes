'''
INPUT
this is a string   
OUTPUT
this-is-a-string
'''
def split_and_join(line):
    line = line.split(" ") #gets converted to list of string
    line = "-".join(line)   #gets back to string here
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
