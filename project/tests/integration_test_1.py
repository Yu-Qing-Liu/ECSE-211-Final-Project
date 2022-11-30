#!/usr/bin/python3

#This file tests for integration of the tower with piston 1 (motor a)

#Object imports
import objects.motor_a as motor_a
import objects.tower as t

#Brick imports
from utils.brick import reset_brick, wait_ready_sensors

import time


try:
    #Initiate motors
    tower = t.Tower()
    piston = motor_a.Motor_A()

    tower.dispense()
    piston.push(0)

    tower.dispense()
    piston.push(1)

    tower.dispense()
    piston.push(2)
except KeyboardInterrupt:
    reset_brick()
    exit(0)