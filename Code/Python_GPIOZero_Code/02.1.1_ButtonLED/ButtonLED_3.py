# !/usr/bin/env python3
# G>PIO Zero example - Button and LED
# Rather more elegant than the previous example, but it does the same thing. 
# Press the button to turn on the LED, release it to turn it off.

from gpiozero import LED, Button
from signal import pause
import sys

led = LED(17)
button = Button(7, hold_time=2, hold_repeat=False, bounce_time=0.1)  # Set hold_time to 2 seconds for the when_held event   

print ('Program is starting...')

button.when_pressed = led.on
button.when_released = led.off
button.when_held = lambda: sys.exit()  # exits Python only

pause()