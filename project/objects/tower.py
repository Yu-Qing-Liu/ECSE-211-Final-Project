from utils.brick import Motor
import time

#A tower object representing the cube tower and its functionalities
class Tower:

    #class variables
    POWER_LIMIT = 100       # Power limit = 100%
    SPEED_LIMIT = 720      # Speed limit = 720 deg per sec (dps)
    rotation = 360
    speed = 200
    sleep_time = rotation/speed

    #Constructor
    def __init__(self):

        #Assign port of motor
        self.motor = Motor("C")
         
    
    #dispenses a cube from the tower
    def dispense(self):
        print("Dispensing a cube")
        #@Todo : code for the dispenser mechanism
        try:
            time.sleep(1)
            self.motor.reset_encoder()                        # Reset encoder to 0 value
            self.motor.set_limits(self.POWER_LIMIT, self.SPEED_LIMIT) # Set the power and speed limits
            self.motor.set_power(0)
            time.sleep(1)

            self.motor.set_dps(self.speed)                              # Set the speed for the motor
            self.motor.set_position_relative(self.rotation)             # Rotate the desired amount of degrees
            time.sleep(self.sleep_time)
            
            self.motor.set_power(0)
        except IOError as error:
            print(error)