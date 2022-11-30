#!/usr/bin/python3

#Object imports
import objects.user as user
import objects.grid as grid
#Brick imports
from utils.brick import reset_brick, wait_ready_sensors



try:
    user = user.User()
    user.start()

    grid = grid.Grid(user.get_inputs)
    response = grid.is_valid()

    if (response == 0):
        print("valid input")
    elif(response == 1):
        print("invalid input: too many cubes")
    elif(response == 2):
        print("invalid input: no cubes inputted")
    
    
    
except KeyboardInterrupt:
    reset_brick()
    exit(0) 