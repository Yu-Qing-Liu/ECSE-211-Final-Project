#!/usr/bin/python3

#Object imports
import objects.motor_b as motor_b

#Brick imports
from utils.brick import reset_brick, wait_ready_sensors


wait_ready_sensors(True)

try:
    #Initiate motors
    motor_b = motor_b.Motor_B()
    #command to push to row 1
    motor_b.push(1)
except KeyboardInterrupt:
    reset_brick()
    exit(0)