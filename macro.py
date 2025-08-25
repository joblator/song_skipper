import pyautogui
import keyboard
import time
dads = True
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
print("starting Program")
keyboard.add_abbreviation('@@','janjoel.bonisch@gmail.com')
while  True:
    if keyboard.is_pressed('F2'):
        print("ending ProgramP")
        quit()
    if keyboard.is_pressed('F1'):
        time.sleep(0.5)
        Skip_song()

