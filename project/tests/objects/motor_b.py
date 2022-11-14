#!/usr/bin/python3
from utils.brick import Motor
import time
import math

#The object Motor_B represents the motor used in vertical pushing.
#Contains push method that rotates the motor based on commands
class Motor_B:

    #class variables
    wheel_radius = 2
    wheel_circumference = 2*math.pi*wheel_radius
    speed = 100 # in dps
    distancePerCell = 4

    POWER_LIMIT = 100       # Power limit = 100%
    SPEED_LIMIT = 720      # Speed limit = 720 deg per sec (dps)
  

    #Constructor
    def __init__(self):
        #Assign port of motor
        self.motor = Motor("B")
 
    
    #Rotate the motor given a command (command can be = to 0,1,2,3,4)
    def push(self,command):
        print("Pushing the cube vertically to position: ", command)
        #Dummy code for testing
        try:

            
            distanceToTravel = (5-command) * self.distancePerCell
            numberOfRotations = distanceToTravel/self.wheel_circumference
            rotation = numberOfRotations * 360
            sleep_time = rotation/self.speed

            time.sleep(1)
            self.motor.reset_encoder()                        # Reset encoder to 0 value
            self.motor.set_limits(self.POWER_LIMIT, self.SPEED_LIMIT) # Set the power and speed limits
            self.motor.set_power(0)
            time.sleep(1)

            #motor moving forward
            self.motor.set_dps(self.speed)                              # Set the speed for the motor
            self.motor.set_position_relative(rotation)             # Rotate the desired amount of degrees
            time.sleep(sleep_time)
            #motor moving backward
            self.motor.set_dps(self.speed)                              # Set the speed for the motor
            self.motor.set_position_relative(-rotation)             # Rotate the desired amount of degrees
            time.sleep(sleep_time)

            self.motor.set_power(0)
        except IOError as error:
            print(error)


