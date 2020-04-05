#!/usr/bin/env python

import sys
import time
sys.path.append('/storage/.kodi/addons/virtual.rpi-tools/lib')
import RPi.GPIO as GPIO
import subprocess

pin=5
oldButtonState1 = True

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.IN)
    return()

try:
    setup()
    while True:
        buttonState1 = GPIO.input(pin)
	if buttonState1 != oldButtonState1 and buttonState1 == False:
	    subprocess.call("shutdown -hP now", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	    sys.exit()
	oldButtonState1 = buttonState1
	time.sleep(0.1)

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
    GPIO.cleanup() # resets all GPIO ports used by this program
