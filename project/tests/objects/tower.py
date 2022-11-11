from utils.brick import Motor
import time

#A tower object representing the cube tower and its functionalities
class Tower:
    #Constructor
    def __init__(self):
        #Assign port of motor
        self.motor = Motor("C")
    
    #dispenses a cube from the tower
    def dispense(self):
        print("Dispensing a cube")
        #@Todo : code for the dispenser mechanism