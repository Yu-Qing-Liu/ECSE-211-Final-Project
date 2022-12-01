#!/usr/bin/python3
from utils.brick import TouchSensor, wait_ready_sensors
from utils.brick import EV3ColorSensor,wait_ready_sensors
from objects.grid import Grid
import time

class Admin:
    #Constructor
    def __init__(self):
        self.inputs = []
        self.cs = EV3ColorSensor(1)

    #Starts the query process using touch sensors
    def start(self):

        wait_ready_sensors(True)
        """
        while True:    
            if self.cs.get_color_name() != "Unknown":
                time.sleep(1.5)
                if self.cs.get_color_name() != "Unknown":
                    time.sleep(1.5)
                    if self.cs.get_color_name() != "Unknown":
                        print("all cubes loaded")
                        break
          """          
        while True:
            row_count = 1
            while row_count <= 5:
                print("Enter the numbers for row #",end=" ")
                print(row_count,end=" ")
                print("in the following format: <0 0 0 0 0>, Press CTRL+C to abort")
                row = input()
                row_arr = row.split()
                if len(row_arr) == 5:
                    i = 0
                    for elem in row_arr:
                        if elem == "0" or elem == "1":
                            i += 1
                        else:
                            print("Invalid input: an input can only be 0 or 1")
                            break
                    if i == 5:
                        for elem in row_arr:
                            self.inputs.append(int(elem))
                        row_count += 1
                else:
                    print("Invalid Input: 0 enter 5 inputs seperated by spaces")

            grid = Grid(self.inputs)
            if grid.is_valid() == 0:
                    break
            elif grid.is_valid() == 1:
                    print("you have exceeded the amount of cubes available, please try again")
                    self.inputs = []       
            elif grid.is_valid() == 2:
                    print("you have to place at least 1 cube, please try again")
                    self.inputs = []
            elif grid.is_valid() == 3:
                    print("Sorry, An unexpected error has occured, please try again")
                    self.inputs = []



    #Retreive the inputs
    def get_inputs(self):
        return self.inputs