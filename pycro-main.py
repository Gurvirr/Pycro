import pyautogui, threading, time
from pynput import keyboard, mouse

pyautogui.FAILSAFE = True

clicking = False

def click_mouse():
    while True:
        x, y = pyautogui.position()
        pyautogui.doubleClick()
        time.sleep(0.01)

def on_press(key):
    key = str(key)
    key = key[1]
    if key == "a":
        print("true")
        clicking = True
        threading.Thread(target = click_mouse).start()

def on_release(key):
    key = str(key)
    key = key[1]
    if key == "a":
        print("false")
        clicking = False

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

# def on_click(x, y, button, pressed):
#     print(button)
#     if button == button.left:
#         clicking = True
#         threading.Thread(target = click_mouse).start()

    
# with mouse.Listener(on_click = on_click) as listener:
#     listener.join()
