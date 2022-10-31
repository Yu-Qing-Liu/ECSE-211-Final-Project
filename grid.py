#Imports
import math
import copy
import itertools
from coordinate import Coordinate

class Grid:
    #Constructor
    def __init__(self, inputs):
        self.inputs = inputs
        self.num_elements = len(inputs)
        self.size = int(math.sqrt(len(inputs)))
    
    #Returns the number of elements in the grid
    def get_num_elements(self):
        return self.num_elements

    #Returns the size of the grid (ex. 5X5 => size = 5)
    def get_size(self):
        return self.size
    
    #Returns a list of all the elements in the grid
    def get_inputs(self):
        return self.inputs
    
    #Returns a list of the grid's rows
    def get_rows(self):
        rows = []
        temp = copy.deepcopy(self.inputs)
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(temp.pop(0))
            rows.append(row)
        return rows

    #Returns a list of the grid's columns
    def get_columns(self):
        columns = []
        temp = copy.deepcopy(self.inputs)
        for i in range(self.size):
            column = []
            k = i
            for j in range(self.size):
                column.append(temp[k])
                k += self.size
            columns.append(column)
        return columns

    #Returns a list of all the block coordinates
    def get_coords(self):

        rows = self.get_rows()
        coords = []

        #Loops through all inputs, filters and transforms inputs into coordinates
        y = self.size - 1
        for row in rows:
            for x,elem in enumerate(row):
                if elem == 1:
                    coords.insert(0,Coordinate(x,y))
                else:
                    coords.insert(0,None)
            y += -1

        coords = [i for i in coords if i is not None]

        return coords


        
            

