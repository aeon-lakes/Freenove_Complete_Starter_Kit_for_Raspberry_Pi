# Button tester

from gpiozero import LED, Button
from signal import pause
import os

led = LED(17)
button = Button(7, hold_time=2, bounce_time=0.1, pull_up=True)

print("Program is starting...")

button.when_pressed = led.on
button.when_released = led.off
button.when_held = lambda: os._exit(0)   # ← force full process exit

pause()