#coding:utf-8
import RPi.GPIO as GPIO
import signal
import atexit
import time

class Steer(object):
    def __init__(self,servoPin=21):
        self.servoPin = servoPin
        atexit.register(GPIO.cleanup)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servoPin, GPIO.OUT, initial=False)
        self.p = GPIO.PWM(self.servoPin, 50)
        self.p.start(5)
    
    def SteerReverse(self):
        self.p.ChangeDutyCycle(10)

    def SteerForward(self):
        self.p.ChangeDutyCycle(6)
    

if __name__ == '__main__':
    Steer1 = Steer(servoPin=21)

    while(1):
        print('zheng')
        Steer1.SteerForward()
        time.sleep(2)
        print('fan')
        Steer1.SteerReverse()
        time.sleep(2)







