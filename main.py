#!/usr/bin/env python

import os
from time import sleep

import RPi.GPIO as GPIO

def ButtonSmashed():
    print "start playing sound"
    os.system('mpg123 -q ./assets/Connection-established-sound-effect.mp3 &')

def ButtonUnsmashed():
    print "stop playing sound"
    os.system('pkill -x -n mpg123')

PrevButtStat = GPIO.LOW

def HandleEdgeDetection(channel):
    global PrevButtStat
    ButtStat = GPIO.input(channel)
    if ButtStat != PrevButtStat:
        PrevButtStat = ButtStat
        if ButtStat == GPIO.HIGH:
            ButtonSmashed()
        elif ButtStat == GPIO.LOW:
            ButtonUnsmashed()

def main():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(18, GPIO.BOTH, callback=HandleEdgeDetection, bouncetime=7)
        while True:
            sleep(0.1)
        return
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()