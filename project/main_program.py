#Object imports
from objects.grid import Grid
from objects.motor_a import Motor_A
from objects.motor_b import Motor_B
#Brick imports
from utils.brick import EV3UltrasonicSensor, reset_brick, wait_ready_sensors
import time


wait_ready_sensors(True)

try:
    #Initiate a test Grid
    grid = Grid([1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1])
    #Get the commands
    col_commands = grid.get_coords("col")

    #Print the commands
    print("Col coords with blocks")
    for coord in col_commands:
        coord.__repr__()

    #Call motor.push depending on the task
    
    
except KeyboardInterrupt:
    reset_brick()
    exit(0)
