# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:37:28 2020

@author: jiang
"""

def GetTemp(SensorID):
    return int(SensorID)


def Alarm():
    print('Alarm')


def CheckSensor():
    HighTemp = 6
    LowTemp = 3
    while True:
        SensorID = input('ID: ')
        if 1 <= int(SensorID) <= 10:
            break
    Temp = GetTemp(SensorID)
    if Temp > HighTemp:
        Alarm()
    elif Temp < LowTemp:
        print('Cold')
    else:
        print('Normal6')
    