import pyautogui
import time
import random
ran = random.randint(100, 500)
while True:
    time.sleep(600000)
    pyautogui.moveTo(pyautogui.position().x+ran,pyautogui.position().y+ran,duration=2)
    print("done")