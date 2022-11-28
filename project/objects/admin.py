#!/usr/bin/python3
from utils.brick import TouchSensor, wait_ready_sensors
import time

class Admin:
    #Constructor
    def __init__(self):
        self.inputs = []

    #Starts the query process using touch sensors
    def start(self):

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