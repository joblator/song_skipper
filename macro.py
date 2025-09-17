import pyautogui
import keyboard
import time
screen_width, screen_height = pyautogui.size()
print(screen_width,screen_height)
screen_width /= 1.9 - (0.03 *((2560 - screen_width) // 640))
screen_height /= 1.1 + (0.03 * ((1440 - screen_height) // 360))
def Skip_song():
    keyboard.press_and_release('alt + tab')
    time.sleep(0.3)
    pyautogui.moveTo(screen_width, screen_height)
    pyautogui.click()
    time.sleep(0.3)
    keyboard.press_and_release('alt + tab')
def stop():
    print("program stopped")
    quit()
print("starting Program press ` to skip songs and ~ to stop the program")
keyboard.add_hotkey("`",Skip_song)
keyboard.add_hotkey("f1",stop)
keyboard.wait()
print("the program finshed")