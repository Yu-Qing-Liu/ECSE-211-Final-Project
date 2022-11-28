#!/usr/bin/python3
#Object imports
from objects.grid import Grid
from objects.motor_a import Motor_A
from objects.motor_b import Motor_B
from objects.tower import Tower
from objects.admin import Admin
from objects.user import User
#Brick imports
from utils.brick import reset_brick, wait_ready_sensors
#Other imports
import time

wait_ready_sensors(True)

try:
    #Initiate motors
    motor_a = Motor_A()
    motor_b = Motor_B()

    #Initiate tower
    cube_tower = Tower()

    #Initialize user GUI and admin console
    admin = Admin()
    user = User()
    
    #Ask user if he wants to use admin or user mode
    while True:
        selection = input("Enter <admin> for admin mode, and <user> for user mode\n")
        if(selection == "user"):
            user.start()
            grid = Grid(user.get_inputs())
            if grid.is_valid() == 0:
                break
            elif grid.is_valid() == 1:
                print("Sorry, you have exceeded the amount of cubes available, please try again")
                user.reset()
            elif grid.is_valid() == 2:
                print("Sorry, you need to use at least 1 cube, please try again")
                user.reset()
            elif grid.is_valid() == 3:
                print("Sorry, an unexpected error has occured, please try again")
                user.reset()
        else:
            user.start()
            grid = Grid(user.get_inputs())
            if(grid.is_valid()):
                break
            else:
                print("Sorry, you have exceeded the amount of cubes available")

    #Print out the grid
    grid.__repr__()

    #Get the commands using row mode (motor_a is place at bottom left)
    #
    #   □ □ □ □ □
    #   □ □ □ □ □
    #   □ □ □ □ □      ^
    #   □ □ □ □ □    motorB
    #   □ □ □ □ □ <- motorA 
    # 

    #Get the list or coordinates in placement order from grid object's method
    commands = grid.get_coords()

    #Algorithm for IDEA #2
    #temp value for y
    y_init = 0

    #pops the coordinates from commands list and evaluates them one by one
    while commands:
        #Store the poped coordinate into a variable called command
        command = commands.pop(0)
        
        #Check if we are on the same row
        if command.get_y() == y_init:
            #Have the cube tower dispense 1x cube
            cube_tower.dispense()
            #create the first row
            #use motor_a object's push method to move the cube to the right position
            motor_a.push(command.get_x())
        else:
            #if we are not on the same row, use motor b to move to the next row
            motor_b.move(command.get_y())
            #Have the cube tower dispense 1x cube
            cube_tower.dispense()
            #start creating the next row
            motor_a.push(command.get_x())
            #we must update the temp value of y to the next row before continuing
            y_init = command.get_y()

except KeyboardInterrupt:
    reset_brick()
    exit(0)
