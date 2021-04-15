'''
import cv2

img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()
'''
import psutil
import pyautogui
import time
import random
import keyboard

var = "VALORANT-Win64-Shipping.exe" in (i.name() for i in psutil.process_iter())
print(var)

while var:
    imgFound = pyautogui.locateOnScreen('WONimg2k.png', confidence=.7)

    if imgFound != None:
        pyautogui.keyDown("shift")
        pyautogui.keyDown("v")

        randomNum = random.randint(6, 9)
        if randomNum == 6:
            pyautogui.press("F6")
        if randomNum == 7:
            pyautogui.press("F7")
        if randomNum == 8:
            pyautogui.press("F8")
        if randomNum == 9:
            pyautogui.press("F9")

        time.sleep(7)
        pyautogui.keyUp("v")
        pyautogui.keyUp("shift")
        time.sleep(20)

    time.sleep(.3)
    var = "VALORANT-Win64-Shipping.exe" in (i.name() for i in psutil.process_iter())
