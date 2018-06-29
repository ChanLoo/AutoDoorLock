import DCMotor
import Steer
import time
import RPi.GPIO as GPIO
import sensor

GPIO.cleanup()
GPIO.setwarnings(False)

doorSteer=Steer.Steer()
doorMotor=DCMotor.DCMotor()
Sensor=sensor.Sensor()


doorMotor.MotorStart()
doorMotor.MotorReverse()
time.sleep(3)
doorSteer.SteerForward()


state=0

while( True):
    try:
        state=Sensor.sensor_stop()
    except:
        print ("Sensor error!")
    if state:
        time.sleep(0.1)
        try:
            state=Sensor.sensor_stop()
        except:
            print ("Sensor error!")
        if state:
            break
        
doorMotor.MotorStop()

doorSteer.SteerReverse()
