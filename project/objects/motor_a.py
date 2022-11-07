from utils.brick import Motor
import time

class Motor_A:
    #Constructor
    def __init__(self):
        #Assign port of motor
        self.motor = Motor("A")
    
    #Rotate the motor given a command (command can be = to 0,1,2,3,4)
    def push(command):
        print("Pushing the block horizontally to position", command)
        #@Todo : implement the correct movements given the command
        