from utils.brick import Motor
import time

#The object Motor_B represents the motor responsible for vertical row pushing. Contains a push method
#that rotates the motor based on commands.
class Motor_B:
    #Constructor
    def __init__(self):
        #Assign port of motor
        self.motor = Motor("B")
        #Assign default position of the robot
        self.position = 0
    
    #Update the robot's position
    def set_position(self,new_position):
        self.position = new_position

    #Rotate the motor given a command (command can be = to 0,1,2,3,4) and based on the robots initial y-position
    def move(self,command):
        print("Moving to row", command,"from ypos",self.position)
        #@Todo : implement the correct movements given the command and based on the robots initial y-position

        #Update the position of the robot based on command given
        self.set_position(command)
        