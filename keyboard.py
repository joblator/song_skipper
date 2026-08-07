import time
import keyboard
from pynput.keyboard import Controller, Key

DEBUG = False
media_keyboard = Controller()

def skip_song():
    media_keyboard.press(Key.media_next)
    media_keyboard.release(Key.media_next)

def previous_song():
    media_keyboard.press(Key.media_previous)
    media_keyboard.release(Key.media_previous)


print("Song Control Program Started")
print("Controls:")
print("  Shift + N = Skip song")
print("  shift + P  = Previous song")

keyboard.add_hotkey('shift+n', skip_song)
keyboard.add_hotkey('shift+p', previous_song)
keyboard.wait()
print("The program finished")