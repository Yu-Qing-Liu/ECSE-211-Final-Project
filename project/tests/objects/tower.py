from utils.brick import Motor
import time

#A tower object representing the cube tower and its functionalities
class Tower:

    #class variables
    POWER_LIMIT = 100       # Power limit = 100%
    SPEED_LIMIT = 720      # Speed limit = 720 deg per sec (dps)
    rotation =368/2
    speed = 350
    sleep_time = rotation/speed
    x = False

    #Constructor
    def __init__(self):

        #Assign port of motor
        self.motor = Motor("C")

    
    #dispenses a cube from the tower
    def dispense(self):
        print("Dispensing a cube")
        #@Todo : code for the dispenser mechanism
        try:
            time.sleep(0.25)
            self.motor.reset_encoder()                        # Reset encoder to 0 value
            self.motor.set_limits(self.POWER_LIMIT, self.SPEED_LIMIT) # Set the power and speed limits
            self.motor.set_power(0)
            time.sleep(0.25)

            self.motor.set_dps(self.speed) 
            self.motor.set_position_relative(self.rotation)
            time.sleep(self.sleep_time)
            
            self.motor.set_dps(self.speed) 
            self.motor.set_position_relative(-self.rotation)
            time.sleep(self.sleep_time)


            self.motor.set_power(0)
        except IOError as error:
            print(error)