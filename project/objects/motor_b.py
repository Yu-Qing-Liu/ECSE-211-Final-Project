from utils.brick import Motor
import time

class Motor_B:
    #Constructor
    def __init__(self):
        #Assign port of motor
        self.motor = Motor("B")
    
    #Rotate the motor given a command (command can be = to 0,1,2,3,4)
    def push(self,command):
        print("Pushing the cubes vertically to position", command)
        #@Todo : implement the correct movements given the command
        
        #Dummy code for testing
        try:
            time.sleep(1)
            # Rotate to push the cubes forward
            self.motor.reset_encoder()
            self.motor.set_dps(200)
            self.motor.set_position_relative(50)
            # Rotate back to original position
            time.sleep(1)
            self.motor.reset_encoder()
            self.motor.set_dps(200)
            self.motor.set_position_relative(-50)
            # Wait for operations to complete
            time.sleep(1.5)
        except IOError as error:
            print(error)