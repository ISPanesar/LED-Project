import os
from time import sleep

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(20, GPIO.OUT, initial=0)
GPIO.setup(21, GPIO.OUT, initial=0)

while True:
    if not GPIO.input(23):
        GPIO.output(20, 1)
        print("LED 1 is on")

    if not GPIO.input(24):
        GPIO.output(21, 1)
        print("LED 2 is on")
    if not GPIO.input(25):
        GPIO.output(20, 0)
        GPIO.output(21, 0)
        import sys
        sys.exit()
    sleep(0.25)
