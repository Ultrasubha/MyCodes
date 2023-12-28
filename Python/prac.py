#file = open("mountBlue.txt", "x")
#file.write("hi tj")
#import os.path as rasta
#if rasta.exists("mountBlue.txt"):
#    file = open("mountBlue.txt", "r+")
#else:
#    file = open("mountBlue.txt", "x")
try:
  f = open("today.txt","r+")
except:
  print("Something went wrong when opening the file")
finally:
    f = open("today.txt","x")
    f.close()