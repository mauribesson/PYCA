# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 17:56:00 2017

@author: Andrea
"""

import serial, time
arduino = serial.Serial("COM5", 9600)
time.sleep(2)
while (True):
    mensaje = arduino.readline()
    print (mensaje)
arduino.close()