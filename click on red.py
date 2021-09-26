

# from pynput.mouse import Button, Controller
from ctypes import windll

import win32api
import win32con

from screeninfo import get_monitors


def get_pixel(x, y):   # timed to take ~ 0.01s
    return tuple(int.to_bytes(windll.gdi32.GetPixel(dc, x, y), 3, "little"))


dc = windll.user32.GetDC(0)

mouseDown = True
red = False
redFallingEdge = False

monitorX = 1920
monitorY = 1080

for m in get_monitors():
    if m.is_primary:
        monitorX = m.width
        monitorY = m.height
        print("found monitor")
        print("res X: "+str(monitorX)+", res Y: "+str(monitorY))

crossX = int(monitorX/2)
crossY = int(monitorY/2)
crossColor = get_pixel(crossX, crossY)
red = False

while True:  # Replace with a case for stopping program
    # if red and crossColor != (255, 0, 0):
    #     redFallingEdge = True
    # else:
    #     redFallingEdge = False
    lastRed = red
    red = (crossColor == (255, 0, 0))
    state_left = win32api.GetKeyState(135)  # Left button down = 0 or 1. Button up = -127 or -128
    crossColor = get_pixel(crossX, crossY)
    if state_left == -127 or state_left == -128:
        # if redFallingEdge:
        #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, crossX, crossY, 0, 0)
        #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, crossX, crossY, 0, 0)
        if lastRed ^ red:
            if red:  # measure the real value for real program
                # Consider using an arduino to emulate a hardware click
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, crossX, crossY, 0, 0)
            else:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, crossX, crossY, 0, 0)
                # remove for actual code
