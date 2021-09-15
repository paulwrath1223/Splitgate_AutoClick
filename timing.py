import time

import win32api

from ctypes import windll

dc = windll.user32.GetDC(0)

crossX = 1920
crossY = 1080
print(f"\ncrossX: {crossX}")
print(f"\ncrossY: {crossY}")


def getpixel(x,y):
    return tuple(int.to_bytes(windll.gdi32.GetPixel(dc,x,y), 3, "little"))




start = time.time()
for i in range(10000):
    state_left = win32api.GetKeyState(135)
end = time.time()
print("Time consumed in working: ",end - start)

