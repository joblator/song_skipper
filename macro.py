import pyautogui
import keyboard
import time
def switch_app():
    keyboard.press_and_release('alt+tab')
    time.sleep(0.3)
def Skip_song():
    while keyboard.is_pressed('`ctrl') or keyboard.is_pressed('left'):
        time.sleep(0.01)
    switch_app()
    time.sleep(0.3)
    keyboard.press_and_release('ctrl+right')
    time.sleep(0.3)
    switch_app()



# if the song is at the very start it will go to the previous song
def go_to_current_song_start():
    switch_app()
    keyboard.press_and_release('ctrl+left')
    time.sleep(0.3)
    switch_app()
    
def previous_song():
    while keyboard.is_pressed('ctrl') or keyboard.is_pressed('right'):
        time.sleep(0.01)
    switch_app()
    time.sleep(0.3)
    keyboard.press_and_release('ctrl+left')
    time.sleep(0.3)
    keyboard.press_and_release('ctrl+left')
    time.sleep(0.3)
    switch_app()
    
def stop():
    print("program stopped")
    quit()
print("Song Control Program Started")
print("Controls:")
print("  Ctrl + Left =  Skip song")
print("  Ctrl + Right  =  Previous song")
print("  ` (backtick) =  Restart current song")
print("  F1 = Stop program\n")
keyboard.add_hotkey('ctrl+left', Skip_song)
keyboard.add_hotkey("f1",stop)
keyboard.add_hotkey("ctrl+right",previous_song)
keyboard.add_hotkey("`",go_to_current_song_start)
keyboard.wait()
print("the program finshed")