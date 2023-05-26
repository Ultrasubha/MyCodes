from pygoogle_image import image as downloader
from datetime import datetime
import webbrowser, os, time, shutil

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

def garbageRemover(path):
    os.chdir(path)
    os.remove(garbage(os.listdir(),1))
    os.remove(garbage(os.listdir(),2))

def imageGenerator(game, pkgs, count, path):         
    #First set of images
    os.chdir(path)
    downloader.download(game, limit=count-3)
    path+="\images\\"+ underScored(game)
    garbageRemover(path)
    time.sleep(5)
    
    #Second set of images
    downloader.download(pkgs, limit=7)
    pkg_pth = path + "\images\\" + pkgs
    garbageRemover(pkg_pth)
    
    #Moving the second set to the first set
    for i in os.listdir():
        shutil.move(i, "..\\..\\")
    os.chdir(path)
    
    #deleting the empty images dir
    shutil.rmtree("images")
    time.sleep(4)

def gamePageOpen(arr):
    webbrowser.open("https://id.heytap.com/v2/profile.html")
    time.sleep(37)
    #pyautogui.hotkey('ctrl', 'w')
    for i in range(10):
        webbrowser.open(arr[i])
        if i==0:
            time.sleep(15) 
        
def OppoEngine(gameCount,accounts,images,path):
    s1="https://games.heytap.com/bbs/index.html?pkgName="
    s3="&region=IN#/home"
    game=[]
    arr=[]
    pkgs=[]
    print("Enter the games : ")
    for _ in range(gameCount):
        game.append(nameFormatter(input()))

    print("\nEnter the packages of games : ")
    for _ in range(gameCount):
            s2=input()
            pkgs.append(s2)
            s=s1+s2+s3
            arr.append(s)
            
    for epoch in range(accounts):
        if epoch<1:
            gamePageOpen(arr)
            time.sleep(7)
            
            #if any previous images exist, delete them
            os.chdir(path)
            if os.path.exists("images"):
                print("Previous images are deleted...")
                shutil.rmtree("images")
            
            for i in range(gameCount):
                imageGenerator(game[i], pkgs[i], images, path)
            print("Image Downloaded successfully :) ")
        else:
            print("Ready to enter the credentials of account",epoch+1," ?")
            if input()=="":
                gamePageOpen(arr)
        
OppoEngine(10,4,17,"D:\OppoGames")