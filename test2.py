#coding:utf-8
import RPi.GPIO as GPIO
import signal
import atexit
import time

print ("import OK!\n")
class Steer(object):
    def __init__(self,servoPin=21):
        self.servoPin = servoPin
        atexit.register(GPIO.cleanup)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.servoPin, GPIO.OUT, initial=False)
        self.p = GPIO.PWM(self.servoPin, 50)
        self.p.start(5)
    
    def SteerForward(self):
        self.p.ChangeDutyCycle(10)

    def SteerReverse(self):
        self.p.ChangeDutyCycle(6)
        
print("Class OK!\n")
try:
    Steer1 = Steer(servoPin=21)
except Exception, e:
    print e
print("Read Pin OK!\n")
Steer1.SteerForward()
print("run OK!\n")
time.sleep(2)
Steer1.SteerReverse()
time.sleep(2)
print ("mission accomplished!")





