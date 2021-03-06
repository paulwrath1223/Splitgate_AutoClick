
# from pynput.mouse import Button, Controller
from ctypes import windll

import win32api
import win32con

from screeninfo import get_monitors


def getpixel(x, y):   # timed to take ~ 0.01s
    return tuple(int.to_bytes(windll.gdi32.GetPixel(dc, x, y), 3, "little"))


dc = windll.user32.GetDC(0)  # no idea wtf this does, but it's used in getPixel


mouseDown = True
red = False
redFallingEdge = False

strength = 20  # Change to tune for sensitivity

redRatioUp = 0
redRatioDown = 0
redRatioRight = 0
redRatioLeft = 0

monitorX = 1920
monitorY = 1080

for m in get_monitors():
    if m.is_primary:
        monitorX = m.width
        monitorY = m.height
        print("found monitor")
        print("res X:  "+str(monitorX)+", res Y:  "+str(monitorY))

crossX = int(monitorX/2)
crossY = int(monitorY/2)
crossColor = getpixel(crossX, crossY)

while True:   # Replace with a case for stopping program
    red = (crossColor == (255, 0, 0))
    state_left = win32api.GetKeyState(135)  # Left button down = 0 or 1. Button up = -127 or -128
    crossColor = getpixel(crossX, crossY)

    if state_left == -127 or state_left == -128:  # Should this be "state_left <= -127"?
        colorUp = (getpixel(crossX, crossY + 10))
        colorDown = (getpixel(crossX, crossY - 10))
        colorRight = (getpixel(crossX + 10, crossY))
        colorLeft = (getpixel(crossX - 10, crossY))

        redRatioUp = int(colorUp[0] / sum(list(colorUp)))
        redRatioDown = int(colorDown[0] / sum(list(colorDown)))
        redRatioRight = int(colorRight[0] / sum(list(colorRight)))
        redRatioLeft = int(colorLeft[0] / sum(list(colorLeft)))

        deltaX = strength * (redRatioRight - redRatioLeft)
        deltaY = strength * (redRatioUp - redRatioDown)

        win32api.SetCursorPos((crossX+deltaX, crossY+deltaY))  # change mouse pos by deltaX and deltaY

    if red:  # measure the real value for real program
        # Consider using an arduino to emulate a hardware click
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, crossX, crossY, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, crossX, crossY, 0, 0)
        # remove for actual code
