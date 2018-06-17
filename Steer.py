#coding:utf-8
import RPi.GPIO as GPIO
import signal
import atexit

class Steer(object, servoPin):
    def __init__(self):
        self.servoPin = servoPin
        self.SteerInit

    def SteerInit(self):
        atexit.register(GPIO.cleanup)
        GPIO.setmode(GPIO.BCM)
        GPIO.set(self.servoPin, GPIO.OUT, initial=False)
        self.p = GPIO.PWM(self.servoPin, 50)
        self.p.start(5)
    
    def SteerForward(self):
        self.p.ChangeDutyCycle(10)

    def SteerReverse(self):
        self.p.ChangeDutyCycle(5)
    

if __name__ == '__main__':
    pass