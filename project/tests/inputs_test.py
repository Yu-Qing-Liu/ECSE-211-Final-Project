#!/usr/bin/python3

#Object imports
import objects.inputs as inputs
#Brick imports
from utils.brick import reset_brick, wait_ready_sensors


try:
    response = inputs.get_inputs()

    if response[0] == 0:
        print("valid input")
        print(response[1])
    if response[0] == 1:
        print("invalid input: too many cubes")
    if response[0] == 2:
        print("invalid input: no cubes inputted")
except KeyboardInterrupt:
    reset_brick()
    exit(0) 