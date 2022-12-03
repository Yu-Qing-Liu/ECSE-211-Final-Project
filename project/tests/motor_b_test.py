#!/usr/bin/python3

#Object imports
import objects.motor_b as motor_b

#Brick imports
from utils.brick import reset_brick, wait_ready_sensors
import time

wait_ready_sensors(True)

try:
   motor_b = motor_b.Motor_B()
   motor_b.move(1)
   motor_b.move(2)
   motor_b.move(3)
   motor_b.move(4)
   motor_b.moveBack()
except KeyboardInterrupt:
    reset_brick()
    exit(0)