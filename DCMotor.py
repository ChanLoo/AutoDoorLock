#coding:utf-8
import RPi.GPIO as GPIO
import time

class DCMotor(object):
    def __init__(self, PWMPin=17, dirPin1=27, dirPin2=22, PWMFreq=100):
        
        
        self.PWMPin = PWMPin
        self.dirPin1 = dirPin1
        self.dirPin2 = dirPin2
        self.PWMFreq = PWMFreq
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PWMPin, GPIO.OUT)
        GPIO.setup(self.dirPin1, GPIO.OUT)
        GPIO.setup(self.dirPin2, GPIO.OUT)
        self.PWM = GPIO.PWM(self.PWMPin, self.PWMFreq)


    def MotorForward(self):
        GPIO.output(self.dirPin1, True)
        GPIO.output(self.dirPin2, False)

    def MotorReverse(self):
        GPIO.output(self.dirPin1, False)
        GPIO.output(self.dirPin2, True)
    
    def SpeedSet(self, speed):
        self.PWM.ChangeDutyCycle(speed)
    
    def MotorStart(self):
        self.PWM.start(100)    # 以输出占空比90%开始
        
    def MotorStop(self):
        self.PWM.start(0)
    
if __name__ == '__main__':
    mt=DCMotor()
    
    while 1 :
        mt.MotorStart()
        print("zheng")
        mt.MotorForward()
        time.sleep(2)
        print("fan")
        mt.MotorReverse()
        time.sleep(2)
        mt.MotorStop()
        time.sleep(2)

