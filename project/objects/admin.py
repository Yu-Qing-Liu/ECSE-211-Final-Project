#!/usr/bin/python3
from utils.brick import TouchSensor, wait_ready_sensors
from utils.brick import EV3UltrasonicSensor
from time import sleep

class Admin:
    #Constructor
    def __init__(self):
        self.inputs = []
        self.us = EV3UltrasonicSensor(2)

    #Starts the query process using touch sensors
    def start(self):

        wait_ready_sensors(True)

        while True:
            if self.us.get_cm() < 5.0:
                sleep(2)
                if self.us.get_cm() < 5.0:
                    print("All cubes loaded")
                    break

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