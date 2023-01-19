import keyboard
import pyautogui
import numpy as np

import time


start_button = "p"

between_tap_delay = 0.00

darkness_threshold = 1

keys = ['a', 's', 'd', 'f']
# https://poki.com/en/g/piano-tiles-2
use_mouse = False
use_win32 = True
height_multiplier = 1.0

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

last_lane = None

def tap_tile(scrot):
    global coords, WIDTH, HEIGHT, keys, last_lane
    for ytemp in range(1, int(HEIGHT * height_multiplier), 5):
        for i in range(4):
            if i == last_lane: continue
            last_lane = i
            x = int(i * WIDTH / 4 + WIDTH / 8)
            y = HEIGHT - ytemp
            
            if scrot[y][x] < darkness_threshold: # if dark
                if use_mouse:
                    if use_win32: # recommended over pyautogui
                        click(x + coords[0], y + coords[1])
                    else:
                        pyautogui.click(x = x + coords[0], y = y + coords[1])
                else:
                    pyautogui.write(keys[i])
                 
                return

while True:
    if keyboard.is_pressed(start_button):
        mousePos1 = pyautogui.position()
        break
    
time.sleep(1)
 
while True:
    if keyboard.is_pressed(start_button):
        mousePos2 = pyautogui.position()
        break

WIDTH = mousePos2.x - mousePos1.x
HEIGHT = mousePos2.y - mousePos1.y

time.sleep(1)

coords = (mousePos1.x, mousePos1.y, mousePos2.x, mousePos2.y)

while True:
    if keyboard.is_pressed(start_button):
        break
    
    scrot = np.array(pyautogui.screenshot(region = (mousePos1.x, mousePos1.y, WIDTH, HEIGHT)))
    scrot = cv2.cvtColor(scrot, cv2.COLOR_BGR2GRAY)
    tap_tile(scrot)
    time.sleep(between_tap_delay)