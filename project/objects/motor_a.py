from utils.brick import Motor
import time

#The object Motor_A represents the motor used in horizontal pushing.
#Contains push method that rotates the motor based on commands
class Motor_A:
    #Constructor
    def __init__(self):
        #Assign port of motor
        self.motor = Motor("A")
    
    #Rotate the motor given a command (command can be = to 0,1,2,3,4)
    def push(self,command):
        print("Pushing the cube horizontally to position", command)
        #@Todo : implement the correct movements given the command
