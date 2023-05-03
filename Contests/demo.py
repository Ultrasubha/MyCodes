from pygoogle_image import image as downloader
from datetime import datetime
import os
import time

def nameFormatter(name):
    s=""
    for i in name:
        if i.isalnum() or i==".":
            s+=i
    s+=" gameplay screenshots"
    return s

def underScored(name):
    s=""
    for i in name:
        if i==" ":
            s+="_"
        else:
            s+=i
    return s

def garbage(names,num):
    for img in names:
        n=len(img)
        for i in range(n):
            if img[i]==str(num) and img[i-1]=="_" and img[i+1]==".":
                return img

def imageGenerator(game,count,path):         
    os.chdir(path)
    downloader.download(game, limit=count)
    path+="\images\\"+ underScored(game)
    os.chdir(path)
    os.remove(garbage(os.listdir(),1))
    os.remove(garbage(os.listdir(),2))
    time.sleep(5)

game=[]
for i in range(10):
    print("Enter the games")
    game.append(nameFormatter(input()))
for i in range(10):
    imageGenerator(game[i], 5, "D:\OppoGames")
    
#date = str(datetime.now())[:10]
#print(os.getcwd())
#os.remove(os.listdir()[0])
#os.remove(os.listdir()[1])
#os.rename("images",date)
#D:\OppoGames\2023-05-02\Korean_Girls