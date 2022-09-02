# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:09:14 2022

@author: jwierman
"""

import serial
import time
import atexit

serialPort = 'COM6'
baudRate = 57600

sleep = .05

try:
    ser = serial.Serial(serialPort, baudRate)
    
except:
    
    serial.Serial(serialPort, baudRate).close()
    print("closing " + serialPort)
    
    #ser = serial.Serial(serialPort, baudRate)
    
    
#!LR1\r\n

def toggleDigitalPin(color, onOff):

    payload = "!LR1\r\n"
    
    som = '!'
    cr = "\r\n"
    
    parameters = [som, 'L', color, onOff,  cr]
    
    payload = "".join(str(i) for i in parameters)
    
    ser.write(str.encode(payload))
    

def partyTime():
    
    
    while True:
        
        toggleDigitalPin('R', 1)
        toggleDigitalPin('G', 0)
        
        time.sleep(sleep)
        
        toggleDigitalPin("Y", 1)
        toggleDigitalPin('R', 0)
        
        time.sleep(sleep)
        
        toggleDigitalPin('G', 1)
        toggleDigitalPin('Y', 0)
        
        time.sleep(sleep)
 
def readFromBoard(pin):
    
    payload = "!LR1\r\n"
    som = '!'
    cr = "\r\n"
    
    parameters = [som, 'P', pin,  cr]
    
    payload = "".join(str(i) for i in parameters)
    
    ser.write(str.encode(payload))
    
    
    #remove "decode()" for full read
    line = ser.readline().decode()

    return (line)

if __name__ == "__main__":
    
    print("")
    

    
    while True:
        
        print(readFromBoard('T'))
        
        time.sleep(.1)
        
        #print("\014")
        print("\033[H\033[J")

        #partyTime()
    
    ser.close()