#!/usr//bin/python
# -*- coding:utf-8 -*-
import smbus
import time

class AD(object):
	def __init__(self):
	    address = 0x48
	    A0=0x40
	    A1=0x41
	    A2=0x42
	    A3=0x43
	    bus = smbus.SMBus(1)
	    
	def AD(self):
            bus.write_byte(address,A0)
            value = bus.read_byte(address)
            vol=value*5.0/255
            print("AOUT:%1.3f " %vol)
            return vol
        
if __name__ == '__main__':
    pass

