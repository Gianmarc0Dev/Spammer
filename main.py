from time import sleep
import pyautogui

print("3 seconds to start")
sleep(3)

times = 100
for i in range(times):
	pyautogui.write("hi")
	pyautogui.press("return")