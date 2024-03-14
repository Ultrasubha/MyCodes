"""
Coded By : Subhadeep Mandal
KnowledgeBase https://pyautogui.readthedocs.io/en/latest/keyboard.html https://datatofish.com/control-keyboard-python/
"""

import webbrowser
import pyautogui
import time
import random
import os

feeling = [
    "Fantastic!",
    "Great!",
    "Wonderful!",
    "Awesome!",
    "Amazing!",
    "Fantastic as always!",
    "Energized and happy!",
    "On top of the world!",
    "Excited and optimistic!",
    "Full of joy!",
    "Blessed and content!",
    "Incredibly happy!",
    "Superb!",
    "Alive and well!",
    "Grateful and joyful!",
    "Thriving!",
    "Fantastic and positive!",
    "Overflowing with happiness!",
    "Radiant!",
    "Uplifted and cheerful!",
    "Pleasantly surprised!",
    "Optimistic and inspired!",
    "Feeling fantastic vibes!",
    "Delightful!",
    "Enthusiastic!",
    "Absolutely fantastic!",
    "Elated and motivated!",
    "Like a champion!",
    "In a state of bliss!",
    "Happy and grateful!",
    "Full of positivity!",
    "In high spirits!",
    "Alive and kicking!",
    "Fantastic and lively!",
    "Ecstatic and content!",
    "Brimming with joy!",
    "Fantastic and blessed!",
    "On cloud nine!",
    "Cheerful and optimistic!",
    "Feeling like a million bucks!",
    "Spectacular!",
    "Pumped and happy!",
    "Overjoyed!",
    "Fantastic and thriving!",
    "Joyful and content!",
    "Super happy and thankful!",
    "In a state of euphoria!",
    "Absolutely delighted!",
    "Happy and at peace!",
]
doubts = [
    "No, everything is going smoothly.",
    "I don't have any doubts at the moment.",
    "Things are progressing well, no blockers.",
    "All clear on my end, no issues.",
    "Smooth sailing, no obstacles.",
    "No doubts or blockers, I'm making good progress.",
    "Everything is on track, no concerns.",
    "I'm not facing any challenges right now.",
    "No issues on my end, making good strides.",
    "All good, no hurdles in my way.",
    "I'm confident in my progress, no doubts.",
    "No blockers, I'm moving forward successfully.",
    "Smooth progress, no need for concern.",
    "I'm clear of doubts and obstacles.",
    "Making steady progress, no issues to report.",
    "No blockers, I'm on the right track.",
    "I have a clear path ahead, no doubts.",
    "No concerns or doubts at this point.",
    "Everything is progressing as expected, no blockers.",
    "No obstacles, I'm advancing smoothly.",
    "I'm confident in my understanding, no doubts.",
    "No issues to report, progressing well.",
    "I'm making good progress, no blockers in sight.",
    "No doubts, I have a clear plan.",
    "Smooth progress, no concerns on my end.",
    "No blockers, I'm moving forward without issues.",
    "I'm on track, no doubts or obstacles.",
    "No concerns at the moment, progress is good.",
    "All clear, no blockers in my way.",
    "I'm confident and progressing well, no doubts.",
    "No obstacles to report, I'm moving forward.",
    "Making good progress, no issues to mention.",
    "No doubts or blockers, everything is on track.",
    "I'm clear of any doubts, progressing smoothly.",
    "No concerns, I'm making positive strides.",
    "All good on my end, no blockers.",
    "I'm focused and moving forward, no doubts.",
    "I'm confident in my progress, no issues.",
    "No doubts, I'm advancing successfully.",
    "Smooth progress, no concerns.",
    "I don't have any doubts or blockers currently.",
    "No issues, progress is going well.",
    "All clear, no obstacles in my way.",
    "I'm confident and focused, no doubts.",
    "No blockers, everything is proceeding as planned.",
    "I'm progressing smoothly, no concerns.",
    "No doubts, I have a clear understanding.",
    "No obstacles, I'm on a positive trajectory.",
    "Making good progress, no blockers to report.",
]
quotes = [
    "Believe you can and you're halfway there. -Theodore Roosevelt",
    "The only way to do great work is to love what you do. -Steve Jobs",
    "Strive not to be a success, but rather to be of value. -Albert Einstein",
    "It always seems impossible until it's done. -Nelson Mandela",
    "Don't watch the clock; do what it does. Keep going. -Sam Levenson",
    "Do what you promise you will do. Don't break a promise you make with yourself -Subhadeep Mandal",
]

GREEN = "\033[92m"
YELLOW = "\033[93m"
END = "\033[0m"


def readMultiLines(stopCharacter="."):
    inp=""
    text=""
    while inp!=stopCharacter:
        text+=inp +"\n"
        inp = input()
    return text.strip()


file = "yesterday.txt"
def yesterday(file):
    if os.path.exists(file):
        with open(file, "r") as file:
            content = file.read()
        return content
    else:
        print(YELLOW + "What did you work on yesterday?\n" + END + "\n(type 'q' without '' in a newline when you are done typing)")
        content = readMultiLines("q")
        with open(file, "w") as file:
            file.write(content)
        return content


print(
    GREEN
    + "MANTRA - A workflow simplifier app.\n@SubhadeepMandal\n\n"
    + random.choice(quotes)
    + "\n\nCopyright (C) Guava_Slice. All rights reserved.\n"
    + END
)

# Start of workflow
os.chdir("D:\_WorkSpace\MyCodes\Python\Automate")
yesterdayWork = yesterday(file)
print(YELLOW + "What is your plan for today?" + END + "\n(type 'q' without '' in a newline when you are done typing)")
todayWork = readMultiLines("q")
webbrowser.open_new_tab("https://checkins.mountblue.io/")
time.sleep(5)
pyautogui.press("tab", presses=4)
pyautogui.press("enter")
time.sleep(4)
pyautogui.press("tab", presses=4)
pyautogui.write(random.choice(feeling))
pyautogui.press("tab")
pyautogui.write(yesterdayWork)
pyautogui.press("tab")
pyautogui.write(todayWork)
pyautogui.press("tab")
pyautogui.write(random.choice(doubts))
pyautogui.press("tab")
pyautogui.press("enter")

with open(file, "w") as file:
    file.write(todayWork)