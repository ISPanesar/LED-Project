import os
from time import sleep

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(5, GPIO.OUT, initial=0)
GPIO.setup(6, GPIO.OUT, initial=0)

while True:
    if not GPIO.input(23):
        GPIO.output(5, 1)

    if not GPIO.input(24):
        GPIO.output(6, 1)

    if not GPIO.input(25):
        import sys

        sys.exit()
    sleep(0.25)
