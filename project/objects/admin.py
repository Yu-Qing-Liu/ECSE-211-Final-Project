#!/usr/bin/python3
from utils.brick import TouchSensor, wait_ready_sensors
from utils.brick import EV3UltrasonicSensor
from time import sleep

class Admin:
    #Constructor
    def __init__(self):
        self.inputs = []
        self.us = EV3UltrasonicSensor(2)
        self.us_data = self.us.get_cm()

    #Starts the query process using touch sensors
    def start(self):

        while self.us_data > 5:
            print("Sorry, there arent enough cubes loaded onto the machine")
            sleep(5)

        for i in range(5):
            row_count = i+1
            print("Enter the numbers for row #",end=" ")
            print(row_count,end=" ")
            print("in the following format: <0 0 0 0 0>, Press CTRL+C to abort")
            row = input()
            row_arr = row.split()
            for elem in row_arr:
                self.inputs.append(int(elem))

    #Retreive the inputs
    def get_inputs(self):
        return self.inputs