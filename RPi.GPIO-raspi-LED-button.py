import os
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

while True:
    if not GPIO.input(23):
        GPIO.output(5, 1)
        pause 1
        GPIO.output(5, 0)

    if not GPIO.input(24):
        GPIO.output(6, 1)
        pause 1
        GPIO.output(6, 0)
    if not GPIO.input(25):
        import sys

        sys.exit()
    sleep(0.25)
