import pyautogui
import time

pyautogui.FAILSAFE

clickLoop = True

while clickLoop:
    for i in range(100):
        pyautogui.PAUSE = 0.01
        pyautogui.moveTo(240, 970)
        pyautogui.leftClick()   
    pyautogui.moveTo(490, 930)
    pyautogui.leftClick()
