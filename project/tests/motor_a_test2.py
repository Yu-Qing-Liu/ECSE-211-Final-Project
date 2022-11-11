#!/usr/bin/python3

#Object imports

import objects.motor_a2 as motor_a
import time

#Brick imports
from utils.brick import reset_brick, wait_ready_sensors


wait_ready_sensors(True)

try:
    #Initiate motors
    motor_a = motor_a.Motor_A()
    motor_a.push(0)


except KeyboardInterrupt:
    reset_brick()
    exit(0)
