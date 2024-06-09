#Joystick_8 from Joystick_8.py
from Joystick_8 import *
from signal import pause
# gpiozero from the package python3-gpiozero
from gpiozero import Button

# Declare a new Joystock
joystick = Joystick_8()
# Writting on the /dev/hidg0
joystick.begin('/dev/hidg0')

def WhenPressed(i:int):
    joystick.press(i)

def WhenReleased(i:int):
    joystick.release(i)

# Pins declaration
buttonsPin = [14,15,2,3,4,23,24]

# lambdas
whenpresseds:list = list()
whenreleaseds:list = list()

# I don't know how to minimize it for the moment...
whenpresseds.append(lambda : WhenPressed(0))
whenreleaseds.append(lambda : WhenReleased(0))
whenpresseds.append(lambda : WhenPressed(1))
whenreleaseds.append(lambda : WhenReleased(1))
whenpresseds.append(lambda : WhenPressed(2))
whenreleaseds.append(lambda : WhenReleased(2))
whenpresseds.append(lambda : WhenPressed(3))
whenreleaseds.append(lambda : WhenReleased(3))
whenpresseds.append(lambda : WhenPressed(4))
whenreleaseds.append(lambda : WhenReleased(4))
whenpresseds.append(lambda : WhenPressed(5))
whenreleaseds.append(lambda : WhenReleased(5))
whenpresseds.append(lambda : WhenPressed(6))
whenreleaseds.append(lambda : WhenReleased(6))


# GpioZero Buttons declaration
buttons:list[Button] = list()

# GpioZero Buttons initialization
for buttonPin in buttonsPin:
    buttons.append(Button(buttonPin))

# Joystick event initialization
for i in range(len(buttonsPin)):
    buttons[i].when_pressed = whenpresseds[i]
    buttons[i].when_released = whenreleaseds[i]

pause()