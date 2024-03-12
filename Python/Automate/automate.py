import time
import pyautogui
import webbrowser

slack_link = "https://app.slack.com/client/TAYFNNJ1K/C023098AEF7"
webbrowser.open(slack_link)

time.sleep(7)
x_coordinate = 784
y_coordinate = 909
pyautogui.click(x_coordinate, y_coordinate)
# pyautogui.write("haha")
# pyautogui.press("enter")