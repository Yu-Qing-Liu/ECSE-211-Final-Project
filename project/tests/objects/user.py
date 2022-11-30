#!/usr/bin/python3
from utils.brick import TouchSensor, wait_ready_sensors
import time

class User:
    #Constructor
    def __init__(self):
        self.inputs = []

    #Starts the query process using touch sensors
    def start(self):

        TOUCH_SENSOR_0 = TouchSensor(1)
        TOUCH_SENSOR_1 = TouchSensor(2)
        wait_ready_sensors(True)

        arr=[]
        arr = [0 for i in range(25)]
        index = 0

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
            if index == 25:
                break

        self.inputs = arr

    def get_inputs(self):
        return self.inputs