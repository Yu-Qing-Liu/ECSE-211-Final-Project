from utils.brick import Motor
import time

#The object Motor_B represents the motor responsible for vertical row pushing. Contains a push method
#that rotates the motor based on commands.
class Motor_B:
    #Constructor
    def __init__(self):
        #Assign port of motor
        self.motor = Motor("B")
    
    #Rotate the motor given a command (command can be = to 0,1,2,3,4)
    def push(self,command):
        print("Moving to row", command)
        #@Todo : implement the correct movements given the command