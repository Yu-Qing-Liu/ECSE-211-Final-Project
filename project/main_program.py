#Object imports
from objects.grid import Grid
from objects.motor_a import Motor_A
from objects.motor_b import Motor_B
#Brick imports
from utils.brick import reset_brick, wait_ready_sensors


wait_ready_sensors(True)

try:
    #Initiate motors
    motor_a = Motor_A()
    motor_b = Motor_B()

    #Initiate a test Grid
    grid = Grid([1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1])

    #Get the commands using row mode (motor_a is place at bottom left)
    #
    #            □ □ □ □ □
    #            □ □ □ □ □
    #            □ □ □ □ □
    #            □ □ □ □ □
    # motorA ->  □ □ □ □ □
    #                ˆ
    #              motorB
    # 

    #Get the list or coordinates in placement order from grid object's method
    commands = grid.get_coords("row")

    #temp value for y
    y_init = commands[0].get_y()

    #pops the coordinates from commands list and evaluates them one by one
    while commands:
        #Store the poped coordinate into a variable called command
        command = commands.pop(0)
        #Check if we are on the same row
        if command.get_y() == y_init:
            #create the row
            #use motor_a object's push method to move the cube to the right position
            motor_a.push(command.get_x())
        else:
            #if we are not on the same row, use motor b to push all the blocks onto the correct row
            motor_b.push(y_init)
            #start creating the next row
            motor_a.push(command.get_x())
            #we must update the temp value of y to the next row before continuing
            y_init = command.get_y()

except KeyboardInterrupt:
    reset_brick()
    exit(0)
