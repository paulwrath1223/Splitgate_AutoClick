

# from pynput.mouse import Button, Controller
from ctypes import windll

import win32api, win32con

from screeninfo import get_monitors


def getpixel(x, y):   # timed to take ~ 0.01s
    return tuple(int.to_bytes(windll.gdi32.GetPixel(dc, x, y), 3, "little"))


# def on_click(x, y, button, pressed):
#     print("on_click")
#     global mouseDown
#     if button == mouse.Button.left:
#         mouseDown = pressed
#

dc = windll.user32.GetDC(0)
# mouse = Controller()

mouseDown = True

monitorX = 1920
monitorY = 1080

for m in get_monitors():
    if m.is_primary:
        monitorX = m.width
        monitorY = m.height
        print("found monitor")

crossX = int(monitorX/2)
crossY = int(monitorY/2)

while True:  # Replace with a case for stopping program
    # state_left = win32api.GetKeyState(135)  # Left button down = 0 or 1. Button up = -127 or -128
    # if state_left == -127 or state_left == -128:

    color = getpixel(crossX, crossY)
    if color == (255, 0, 0):  # measure the real value for real program


        # Consider using an arduino to emulate a hardware click
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, crossX, crossY, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, crossX, crossY, 0, 0)
        # remove for actual code
