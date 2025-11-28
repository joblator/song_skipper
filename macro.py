import time
import keyboard
from pynput.keyboard import Controller, Key

DEBUG = False
media_keyboard = Controller()

def skip_song():
    if DEBUG:
        print("[ENTER] skip_song")
    while keyboard.is_pressed('ctrl') or keyboard.is_pressed('right'):
        time.sleep(0.01)
    media_keyboard.press(Key.media_next)
    media_keyboard.release(Key.media_next)
    if DEBUG:
        print("[EXIT] skip_song")

def previous_song():
    if DEBUG:
        print("[ENTER] previous_song")
    while keyboard.is_pressed('ctrl') or keyboard.is_pressed('left'):
        time.sleep(0.01)
    media_keyboard.press(Key.media_previous)
    media_keyboard.release(Key.media_previous)
    if DEBUG:
        print("[EXIT] previous_song")

def go_to_current_song_start():
    if DEBUG:
        print("[ENTER] go_to_current_song_start")
    while keyboard.is_pressed('`'):
        time.sleep(0.01)
    media_keyboard.press(Key.media_previous)
    media_keyboard.release(Key.media_previous)
    time.sleep(0.1)
    media_keyboard.press(Key.media_next)
    media_keyboard.release(Key.media_next)
    if DEBUG:
        print("[EXIT] go_to_current_song_start")

def stop_program():
    if DEBUG:
        print("[ENTER] stop_program")
    print("Program stopped")
    if DEBUG:
        print("[EXIT] stop_program")
    quit()

print("Song Control Program Started")
print("Controls:")
print("  Ctrl + Right = Skip song")
print("  Ctrl + Left  = Previous song")
print("  ` (backtick) = Restart current song")
print("  F1 = Stop program\n")

keyboard.add_hotkey('ctrl+right', skip_song)
keyboard.add_hotkey('ctrl+left', previous_song)
keyboard.add_hotkey('`', go_to_current_song_start)
keyboard.add_hotkey('f1', stop_program)

keyboard.wait()
print("The program finished")