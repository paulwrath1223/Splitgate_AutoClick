import time

import win32api
from pynput.mouse import Button, Controller
from ctypes import windll

mouse = Controller()


width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
crossX = int((width + 1) / 2)  # Note to future self: add offset for the
crossY = int((height + 1) / 2)

dc = windll.user32.GetDC(0)


def getpixel(x, y):   # timed to take ~ 0.01s
    return tuple(int.to_bytes(windll.gdi32.GetPixel(dc, x, y), 3, "little"))


while True:
    # state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    # if state_left==-127 or state_left==-128:
    #     print('click')
    mouseX = int(2.5*(mouse.position[0]))
    mouseY = int(2.5*(mouse.position[1]))
    if mouseX >= 3840:
        mouseX = 3839
    if mouseY >= 2160:
        mouseY = 2159
    color = getpixel(mouseX, mouseY)
    red = color[0]
    blue = color[1]
    green = color[2]

    print("Mouse pos: X: "+str(mouseX)+"\tY: "+str(mouseY)+"\ncolor: R: "+str(red)+"\tB: "+str(blue)+"\tG: "+str(green))
    time.sleep(0.2)
