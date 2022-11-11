#!/usr/bin/python3
from utils.brick import Motor
import time
import math

#The object Motor_A represents the motor used in horizontal pushing.
#Contains push method that rotates the motor based on commands
class Motor_A:

    #class variables
    wheel_radius = 2
    wheel_circumference = 2*math.pi*wheel_radius
    distancePerCell = 4

    #Constructor
    def __init__(self):

        POWER_LIMIT = 100       # Power limit = 100%
        SPEED_LIMIT = 720      # Speed limit = 720 deg per sec (dps)

        #Assign port of motor
        self.motor = Motor("A")
        time.sleep(1)
        self.motor.reset_encoder()                        # Reset encoder to 0 value
        self.motor.set_limits(POWER_LIMIT, SPEED_LIMIT) # Set the power and speed limits
        self.motor.set_power(0)
    
    #Rotate the motor given a command (command can be = to 0,1,2,3,4)
    def push(self,command):
        print("Pushing the cube horizontally to position: ", command)
        try:
            distanceToTravel = (5-command) * self.distancePerCell
            numberOfRotations = distanceToTravel/self.wheel_circumference
            rotation = numberOfRotations * 360
            sleep_time = (5-command)*2

            #motor moving forward
            print("moving forward")
            self.motor.set_power(-5)                              # Set the speed for the motor
            self.motor.set_position_relative(rotation)
            time.sleep(sleep_time)
            self.motor.set_power(0)

            #motor moving backward
            print("moving backward")
            self.motor.set_power(5)                              # Set the speed for the motor
            self.motor.set_position_relative(rotation)
            time.sleep(sleep_time)
            self.motor.set_power(0)

        except IOError as error:
            print(error)
