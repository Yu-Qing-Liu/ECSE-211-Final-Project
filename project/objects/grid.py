#Imports
import math
import copy
from objects.coordinate import Coordinate

# A grid object used to represent the grid. Contains methods related to the grid properties
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

    #Returns a list of all the block coordinates
    def get_coords(self):
        """Returns a list of coordinates of block placement"""

        coords = []

        rows = self.get_rows()

        #Loops through all inputs, filters and transforms inputs into coordinates
        y = 0
        for row in rows:
            x = self.size - 1
            for elem in row:
                if elem == 1:
                    coords.append(Coordinate(x,y))
                    x -= 1
                else:
                    x -= 1
            y += 1

        return coords

    #Prints out the grid
    def __repr__(self):
        rows = self.get_rows()
        for row in rows:
            print(row)

