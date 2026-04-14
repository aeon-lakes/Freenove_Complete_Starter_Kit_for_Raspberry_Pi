#!/usr/bin/env python3

# Clean exit state machine example for a light/water level indicator using an LED and a button.

from gpiozero import LED, Button
import time
import sys

led = LED(17)
button = Button(26, pull_up=True)

OFF = "OFF"
ON = "ON"
BLINK = "BLINK"

state = OFF
blink_interval = 0.2
last_blink_time = time.time()

button_was_pressed = False
press_start_time = 0
long_press_time = 2.0   # seconds required to exit

print("Program running...")
print("Initial state:", state)

try:
    while True:

        # ---- STATE BEHAVIOR ----
        if state == OFF:
            led.off()

        elif state == ON:
            led.on()

        elif state == BLINK:
            current_time = time.time()
            if current_time - last_blink_time >= blink_interval:
                led.toggle()
                last_blink_time = current_time

        # ---- BUTTON HANDLING ----
        if button.is_pressed and not button_was_pressed:
            press_start_time = time.time()
            button_was_pressed = True

        if not button.is_pressed and button_was_pressed:
            press_duration = time.time() - press_start_time
            button_was_pressed = False

            if press_duration >= long_press_time:
                print("Long press detected. Exiting gracefully...")
                break
            else:
                # Short press → change state
                if state == OFF:
                    state = ON
                elif state == ON:
                    state = BLINK
                elif state == BLINK:
                    state = OFF

                print("New state:", state)

except KeyboardInterrupt:
    print("\nInterrupted by user.")

finally:
    print("Cleaning up...")
    led.off()
    sys.exit(0)
    button_was_pressed = False