import pygame
import sys
import time
import keyboard
from pynput.keyboard import Controller, Key
media_keyboard = Controller()
pygame.init()
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)
controller.init()
# Make sure a controller is connected
if pygame.joystick.get_count() == 0:
    print("No PS4 controller detected!")
    sys.exit()

print("Controller connected:", controller.get_name())

num_buttons = controller.get_numbuttons()
print("Total buttons:", num_buttons)
DEBUG = False
button_last_time = [0] * num_buttons
DELAY = 0.5  # seconds between repeated prints


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
# --- Anti-spam timing table ---

while True:
    pygame.event.pump()

    current_time = time.time()

    for btn in range(num_buttons):
        state = controller.get_button(btn)

        if state:
            # only print if enough time has passed
            if current_time - button_last_time[btn] >= DELAY:
                print(f"Button {btn} pressed")
                button_last_time[btn] = current_time

                # SHARE button = usually 8
                if btn == 4:
                    previous_song()
                if btn == 6:
                    skip_song()

    time.sleep(0.01)