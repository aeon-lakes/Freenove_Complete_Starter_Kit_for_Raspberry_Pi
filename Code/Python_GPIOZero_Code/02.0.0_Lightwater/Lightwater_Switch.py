#!/usr/bin/env python3
# Simple state machine example for a light/water level indicator using an LED and a button.

 from gpiozero import LED, Button
import time

led = LED(17)
button = Button(26, pull_up=True)

OFF = "OFF"
ON = "ON"
BLINK = "BLINK"

state = OFF
blink_interval = 0.5
last_blink_time = time.time()

button_was_pressed = False

print("Program running...")
print("Initial state:", state)

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

    # ---- STATE TRANSITION ----
    if button.is_pressed and not button_was_pressed:
        if state == OFF:
            state = ON
        elif state == ON:
            state = BLINK
        elif state == BLINK:
            state = OFF

        print("New state:", state)
        button_was_pressed = True

    if not button.is_pressed:
        button_was_pressed = False