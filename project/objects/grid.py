#Imports
import math
import copy
from objects.coordinate import Coordinate

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
    
    #Returns a list of the grid's rows from 1rst row to last row
    def get_rows(self):
        rows = []
        temp = copy.deepcopy(self.inputs)
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(temp.pop(0))
            rows.append(row)
        return rows

    #Returns a list of the grid's rows from last row to first row
    def get_rows_reverse(self):
        rows = []
        temp = copy.deepcopy(self.inputs)
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.insert(0,temp.pop(0))
            rows.insert(0,row)
        return rows

    #Returns a list of all the block coordinates (Idea #1)
    def get_coords_1(self):
        """Returns a list of coordinates of block placement"""

        coords = []

        rows = self.get_rows()

        #Loops through all inputs, filters and transforms inputs into coordinates
        y = self.size - 1
        for row in rows:
            x = self.size - 1
            for elem in reversed(row):
                if elem == 1:
                    coords.append(Coordinate(x,y))
                    x -= 1
                else:
                    x -= 1
            y -= 1

        return coords

    #Returns a list of all the block coordinates (Idea #2)
    def get_coords_2(self):
        """Returns a list of coordinates of block placement"""

        coords = []

        rows = self.get_rows_reverse()

        #Loops through all inputs, filters and transforms inputs into coordinates
        y = 0
        for row in rows:
            for x,elem in enumerate(row):
                if elem == 1:
                    coords.append(Coordinate(4-x,y))
                else:
                    pass
            y += 1

        return coords

    #Returns true if the grid is valid, false otherwise
    def is_valid(self):
        cubes = 0
        for input in self.inputs:
            if input == 1:
                cubes += 1
        #error codes: 0 for success, 1 for too many cubes, 2 for no cubes and 3 for unexpected error
        if cubes <= 15 and cubes >=1:
            return 0                
        elif cubes > 15:
            return 1
        elif cubes < 1:
            return 2
        else:
            return 3



    #Prints out the grid
    def __repr__(self):
        rows = self.get_rows()
        for row in rows:
            print(row)

