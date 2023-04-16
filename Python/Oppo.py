import webbrowser
import time
s1="https://games.heytap.com/bbs/index.html?pkgName="
s3="&region=IN#/home"
arr=[]
for _ in range(10):
        s2=input()
        s=s1+s2+s3
        arr.append(s)
for __ in range(4):
    if input()=="":
        webbrowser.open("https://id.heytap.com/v2/profile.html")
        time.sleep(37)
        #pyautogui.hotkey('ctrl', 'w')
        for i in range(10):
            webbrowser.open(arr[i])
            if i==0:
                time.sleep(15) 