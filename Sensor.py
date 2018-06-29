#!/usr/bin/python
# _*_coding:utf-8_*_

import RPi.GPIO as GPIO
import time

class Sensor(object):
    def __init__(self, sensorPin=18):
        self.sensorPin = sensorPin
        GPIO.setmode(GPIO.BCM)
        #GPIO.cleanup()
        GPIO.setup(self.sensorPin, GPIO.IN)
        
    def sensor_stop(self):
        if GPIO.input(self.sensorPin)==GPIO.HIGH:
            print ('detect the boundary!')
            return 1
        else:
            return 0
	
        
if __name__ == '__main__':
    a=Sensor()
    while 1:
        i=a.sensor_stop()
        print(i)
            
    
    




