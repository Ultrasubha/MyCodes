from pygoogle_image import image as downloader
from datetime import datetime
import os
import webbrowser
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

def coreProcess(arr):
    webbrowser.open("https://id.heytap.com/v2/profile.html")
    time.sleep(37)
    #pyautogui.hotkey('ctrl', 'w')
    for i in range(10):
        webbrowser.open(arr[i])
        if i==0:
            time.sleep(15) 
        
s1="https://games.heytap.com/bbs/index.html?pkgName="
s3="&region=IN#/home"
game=[]
arr=[]
print("Enter the games : ")
for _ in range(10):
    game.append(nameFormatter(input()))

print("Enter the packages of games : ")
for _ in range(10):
        s2=input()
        s=s1+s2+s3
        arr.append(s)
        
for epoch in range(4):
    if epoch<1:
        coreProcess(arr)
        time.sleep(7)
        for i in range(10):
            imageGenerator(game[i], 5, "D:\OppoGames")
        print("Image Downloaded successfully :) ")
    else:
        print("Ready to enter the credentials of account",epoch+1,"?")
        if input()=="":
            coreProcess(arr)
        