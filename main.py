from time import sleep
import pyautogui #pip install pyautogui

print("3 seconds to start")
sleep(3)

times = 100
for i in range(times):
	pyautogui.write("hi")
	pyautogui.press("return")
#check out my video on https://youtu.be/V4mPfikiz4Y
