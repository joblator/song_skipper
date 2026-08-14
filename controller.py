import pygame
import sys
import time
from pynput.keyboard import Controller, Key
media_keyboard = Controller()
pygame.init()
pygame.joystick.init()
def connect_controller():
    if pygame.joystick.get_count() == 0:
        print("returned None")
        return None
    print("gello")
    controller = pygame.joystick.Joystick(0)
    controller.init()
    print("Controller connected:", controller.get_name())
    return controller
# Make sure a controller is connected
controller = connect_controller()
if pygame.joystick.get_count() == 0:
    print("No PS4 controller detected!")
    sys.exit()

print("Controller connected:", controller.get_name())

num_buttons = controller.get_numbuttons()
print("Total buttons:", num_buttons)
DEBUG = False
button_last_time = [0] * num_buttons
DELAY = 0.5  # seconds between repeated prints
print("press Share to go to previos song")
print("press Dpad to skip song")

def skip_song():
    media_keyboard.press(Key.media_next)
    media_keyboard.release(Key.media_next)

def previous_song():
    media_keyboard.press(Key.media_previous)
    media_keyboard.release(Key.media_previous)

while True:
    pygame.event.pump()


    current_time = time.time()
    if not controller or pygame.joystick.get_count() == 0:
        controller = connect_controller()
    else:
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
                    if btn == 15:
                        skip_song()                 

    time.sleep(0.01)