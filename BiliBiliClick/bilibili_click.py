import win32api
import win32gui
import win32con
import time, random

count = 0
while True:
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    duration = random.random()
    time.sleep(duration/2)
    count += 1
    if count % 100 == 0: print(count)
