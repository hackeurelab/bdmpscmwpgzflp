#!/usr/bin/env python

import os
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

def ButtonSmashed():
    print "start playing sound"
    os.system('mpg123 -q Connection-established-sound-effect.mp3 &')

def ButtonUnsmashed():
    print "stop playing sound"

def HandleEdgeDetection(channel):
    print GPIO.input(channel)
    if GPIO.input(channel):
        ButtonSmashed()
    else:
        ButtonUnsmashed()

def main():
    GPIO.add_event_detect(18, GPIO.BOTH, callback=HandleEdgeDetection, bouncetime=200)
    while True:
        pass
    return

if __name__ == '__main__':
    main()