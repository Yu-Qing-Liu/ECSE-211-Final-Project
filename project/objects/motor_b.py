#!/usr/bin/python3
from utils.brick import Motor
import time
import math

#The object Motor_B represents the motor responsible for vertical row pushing. Contains a push method
#that rotates the motor based on commands.
class Motor_B:

    #class variables
    wheel_radius = 5
    wheel_circumference = 2*math.pi*wheel_radius
    speed = 50 # in dps
    distancePerCell = 4



    #Constructor
    def __init__(self):
        POWER_LIMIT = 100       # Power limit = 100%
        SPEED_LIMIT = 720      # Speed limit = 720 deg per sec (dps)

        #Assign port of motor
        self.motor = Motor("B")
        #Assign default position of the robot
        self.position = 0
        time.sleep(1)
        self.motor.reset_encoder()                        # Reset encoder to 0 value
        self.motor.set_limits(POWER_LIMIT, SPEED_LIMIT) # Set the power and speed limits
        self.motor.set_power(0)
  
    #Update the robot's position
    def set_position(self,new_position):
        self.position = new_position
    
    #Rotate the motor given a command (command can be = to 0,1,2,3,4)
    def move(self,command):
        print("Moving the robot vertically to row: ", command)
        #@Todo : implement the correct movements given the command
        
        #Dummy code for testing
        try:
            distanceToTravel = (command - 5) * self.distancePerCell
            numberOfRotations = distanceToTravel/self.wheel_circumference
            rotation = numberOfRotations * 360
            sleep_time = rotation/self.speed

            #motor moving forward
            self.motor.set_dps(self.speed)                              # Set the speed for the motor
            self.motor.set_position_relative(rotation) 
            time.sleep(sleep_time)
            #motor moving forward
            self.motor.set_dps(self.speed)                              # Set the speed for the motor
            self.motor.set_position_relative(-rotation)
            time.sleep(sleep_time)
            
            #Update the position of the robot based on command given
            self.set_position(command)
            
        except IOError as error:
            print(error)

