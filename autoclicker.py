import pyautogui
import time

pyautogui.FAILSAFE = True

clickLoop = True
clickCount = 0

while clickLoop:
    for i in range(500):
        pyautogui.PAUSE = 0.01
        pyautogui.moveTo(1280, 746)
        pyautogui.leftClick()
        clickCount += 1
        print(f"Click: {clickCount}")
        
    pyautogui.moveTo(185, 960)
    pyautogui.leftClick()
    pyautogui.moveTo(1280, 1065)
    pyautogui.leftClick()
    
    clickCount = 0  # Reset click count at the end of each loop
