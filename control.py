#!/usr/bin/env python
# Original Author: Edoardo Paolo Scalafiotti <edoardo849@gmail.com>
# Modified to work on libreElec by Gary Beldon

import os
import time
import signal
import sys
sys.path.append('/storage/.kodi/addons/virtual.rpi-tools/lib')
import RPi.GPIO as GPIO
import subprocess

maxTemp = 60 # The temperature in Celsius after which we trigger the fan
minTemp = 50 # Temp when we turn the fan off
sleepTime = 5 # Read the temperature every n sec, increase or decrease this limit if you want

#logfile = "/storage/.kodi/temp/power.log"
pin = 32 # The pin ID, edit here to change it
fanRunning = False

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
#    logging("Initializing.")
    return()

def getCPUtemperature():
    temp = subprocess.check_output(['vcgencmd', 'measure_temp'])[5:-3]
    return temp
def fanON():
    GPIO.output(pin, True)
    return()
def fanOFF():
    GPIO.output(pin, False)
    return()
def checkTemp():
    global fanRunning
    CPUtemp = float(getCPUtemperature())
    if fanRunning==False and CPUtemp>maxTemp:
        fanRunning = True
        fanON()
#        logging("Temp=" + str(CPUtemp) + "C. Switching fan On.")
    if fanRunning==True and CPUtemp<minTemp:
        fanRunning = False
        fanOFF()
#        logging("Temp=" + str(CPUtemp) + "C. Switching fan Off.")
    return()
def logging(message):
    logfilehandle=open(logfile,'a')
    logfilehandle.write(time.strftime("%c") + " :- " + message + "\n")
    logfilehandle.close()
    return();

try:
    setup() 
    while True:
        checkTemp()
        time.sleep(sleepTime)

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
#    logging("Terminating.")
    GPIO.cleanup() # resets all GPIO ports used by this program
