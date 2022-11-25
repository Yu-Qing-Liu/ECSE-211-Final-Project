#!/usr/bin/python3
from utils.brick import Motor
import time
import math

#The object Motor_A represents the motor used in horizontal pushing.
#Contains push method that rotates the motor based on commands
class Motor_B:

    #class variables
    wheel_radius = 2
    wheel_circumference = 2*math.pi*wheel_radius
    speed = 200 # in dps
    distancePerCell = 4

    POWER_LIMIT = 100       # Power limit = 100%
    SPEED_LIMIT = 720      # Speed limit = 720 deg per sec (dps)

    #Constructor
    def __init__(self):
        #Assign port of motor
        self.motorB = Motor("B")
        self.motorD = Motor("D")
        #Initial position
        self.position = 0

    #Update the initial position of the robot
    def update(self, new_position):
        self.position = new_position
            
    def move(self,command):
        print("Moving the robot to position:", command,"From position",self.position)
        distanceToTravel = 4.5*(command - self.position)
        numberOfRotations = distanceToTravel/self.wheel_circumference
        rotation = numberOfRotations * 360
        sleep_time = rotation/self.speed
        
        time.sleep(0.2)
        self.motorD.reset_encoder()                        # Reset encoder to 0 value
        self.motorD.set_limits(self.POWER_LIMIT, self.SPEED_LIMIT) # Set the power and speed limits
        self.motorD.set_power(0)
        self.motorB.reset_encoder()                        # Reset encoder to 0 value
        self.motorB.set_limits(self.POWER_LIMIT, self.SPEED_LIMIT) # Set the power and speed limits
        self.motorB.set_power(0)
        time.sleep(0.2)

        #motor moving
        self.motorB.set_dps(self.speed)                              # Set the speed for the motor
        self.motorB.set_position_relative(-rotation)             # Rotate the desired amount of degrees
        self.motorD.set_dps(self.speed)                              # Set the speed for the motor
        self.motorD.set_position_relative(rotation)             # Rotate the desired amount of degrees
        time.sleep(sleep_time)

        self.update(command)

