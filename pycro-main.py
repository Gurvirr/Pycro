import pyautogui, threading, time
from pynput import keyboard, mouse

pyautogui.FAILSAFE = True

clicking = False

def click_mouse():
    global clicking
    while clicking == True:
        print("running")
        x, y = pyautogui.position()
        pyautogui.doubleClick()
        time.sleep(0.01)

def on_press(key):
    global clicking
    if key == key.shift:
        print("true")
        clicking = True
        threading.Thread(target = click_mouse).start()

def on_release(key):
    global clicking
    if key == key.shift:
        print("false")
        clicking = False

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
