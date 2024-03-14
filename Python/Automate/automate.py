import os, time, pyautogui, webbrowser
from datetime import datetime

slack_link = "https://app.slack.com/client/TAYFNNJ1K/C023098AEF7"
webbrowser.open(slack_link)

time.sleep(4)
x_coordinate = 784
y_coordinate = 909
pyautogui.click(x_coordinate, y_coordinate)
os.chdir("D:\_WorkSpace\MyCodes\Python\Automate")
text = ""
with open("yesterday.txt", "r") as file:
    content = file.read()
    text = "Update@*" + datetime.today().strftime('%d-%m-%Y') + "*\n\n" + content
time.sleep(1)
pyautogui.write(text)
time.sleep(2)
pyautogui.press("enter")
