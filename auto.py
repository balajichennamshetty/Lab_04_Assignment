import pyautogui
import time
time.sleep(5)
for line in open ("text.txt","r"):
    pyautogui.typewrite(line)
