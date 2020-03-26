import pyautogui
import time
import sys
from datetime import datetime

pyautogui.FAILSAFE = False # disables the fail-safe

def move_mouse(w, l):
    for i in range(1):
        pyautogui.moveTo(w, l, duration=0.25)
        pyautogui.moveTo(w+5, l+5, duration=0.25)
        pyautogui.moveTo(w, l, duration=0.25)

# to check for the user argument
if ((len(sys.argv) < 2) or int(sys.argv[1]) < 1):
    sleep_minutes = 3
else:
    sleep_minutes = int(sys.argv[1])

# move the mouse every 3 minutes / user provided number
while True:
    time.sleep(sleep_minutes * 60)
    width, length = pyautogui.position()
    move_mouse(width, length)
    print("Movement at {}".format(datetime.now().time()))