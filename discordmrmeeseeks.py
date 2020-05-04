import pyautogui
import time

x = 700000
time.sleep(5)

while (x > 0): 
 pyautogui.write('I am MR MEESEEEEEKS', interval=.01)
 pyautogui.press('enter')
 x = x - 1
 xmore = str(x)
 pyautogui.write('I will say this ' + xmore + ' more times', interval=.01)
 pyautogui.press('enter')
 time.sleep(62)