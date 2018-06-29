import DCMotor
import Steer
import time
import RPi.GPIO as GPIO
import sensor
import AD

GPIO.cleanup()
GPIO.setwarnings(False)

doorSteer=Steer.Steer()
doorMotor=DCMotor.DCMotor()
Sensor=sensor.Sensor()
#AD=AD.AD()

doorSteer.SteerForward()
time.sleep(1)
doorMotor.MotorStart()
doorMotor.MotorForward()
time.sleep(6)

doorSteer.SteerReverse()
state=0

while( True):
    #VOLTAGE=AD.AD()
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
