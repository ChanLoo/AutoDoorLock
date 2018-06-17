#coding:utf-8
import RPi.GPIO as GPIO

class DCMotor(object, PWMPin, dirPin1, dirPin2, PWMFreq):
    def __init__(self):
        self.PWMPin = PWMPin
        self.dirPin1 = dirPin1
        self.dirPin2 = dirPin2
        self.PWMFreq = PWMFreq
        self.DCMotorInit

    def DCMotorInit(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PWMPin, GPIO.OUT)
        GPIO.setup(self.dirPin1, GPIO.OUT)
        GPIO.setup(self.dirPin2, GPIO.OUT)
        self.PWM = GPIO.PWM(self.PWMPin, self.PWMFreq)
        GPIO.output(self.dirPin1, True)
        GPIO.output(self.dirPin2, False)

    def MotorForward(self):
        GPIO.output(self.dirPin1, True)
        GPIO.output(self.dirPin2, False)

    def MoterReverse(self):
        GPIO.output(self.dirPin1, False)
        GPIO.output(self.dirPin2, True)
    
    def SpeedSet(self, speed):
        self.PWM.ChangeDutyCycle(speed)
    
    def MoterStart(self):
        self.PWM.start(90)    # 以输出占空比90%开始
    
if __name__ == '__main__':
    pass