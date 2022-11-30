#!/usr/bin/python3

#Object imports
import objects.motor_a as motor_a


#Brick imports
from utils.brick import reset_brick, wait_ready_sensors


wait_ready_sensors(True)

try:
    #Initiate motors
    motor_a = motor_a.Motor_A()
    #command to push to pos 0
    motor_a.push(4)
    motor_a.push(3)
    motor_a.push(2)
    motor_a.push(1)
    motor_a.push(0)

except KeyboardInterrupt:
    reset_brick()
    exit(0)
