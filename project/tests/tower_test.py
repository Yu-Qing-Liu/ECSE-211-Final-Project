#!/usr/bin/python3

#Object imports
import objects.tower as tower

#Brick imports
from utils.brick import reset_brick, wait_ready_sensors, TouchSensor
import time

ts = TouchSensor(1)
wait_ready_sensors(True)

try:
    #Initiate motors
    t = tower.Tower()
    while (True):
        time.sleep(0.25)
        if ts.is_pressed:
            print("pressed")
            t.dispense()
except KeyboardInterrupt:
    reset_brick()
    exit(0)