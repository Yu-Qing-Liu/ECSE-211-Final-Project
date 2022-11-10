#!/usr/bin/python3
from utils.brick import Motor, TouchSensor, wait_ready_sensors
import time

def get_inputs():

    TOUCH_SENSOR_0 = TouchSensor(1)
    TOUCH_SENSOR_1 = TouchSensor(2)
    wait_ready_sensors(True)


    arr=[]
    arr = [0 for i in range(10)]
    index = 0
    sum = 0

    while True:
        time.sleep(0.2)
        if TOUCH_SENSOR_1.is_pressed():
            print("1")
            arr[index] = 1
            index += 1
            time.sleep(0.1)
        if TOUCH_SENSOR_0.is_pressed():
            print("0")
            index += 1
            time.sleep(0.1)
        if index == 10:
            break

    for i in arr:
        sum += i
           
    if sum > 7:
        return (1,None)  # 1 is the error code for too many cubes
    if sum < 1:
        return (2,None) # 2 is the error code for 0 cubes
    return (0,arr) # 0 is the success code 