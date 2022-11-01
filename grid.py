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
            rows.insert(0,row)
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
            columns.insert(0,column)
        return columns

    #Returns a list of all the block coordinates
    def get_coords(self,direction):
        """Returns a list of coordinates of block placement, takes in a string parameter <row> or <col>
            Row mode : Horizontal block placement starting at (4,4)
            Column mode: Vertical block placement starting at (4,4)
        """

        coords = []

        if direction == "row":
            rows = self.get_rows()

            #Loops through all inputs, filters and transforms inputs into coordinates
            y = self.size - 1
            for row in rows:
                x = self.size - 1
                for elem in row:
                    if elem == 1:
                        coords.append(Coordinate(x,y))
                        x += -1
                    else:
                        x += -1
                y += -1

            return coords

        elif direction == "col":
            cols = self.get_columns()

            #Loops through all inputs, filters and transforms inputs into coordinates
            x = self.size - 1
            for col in cols:
                y = self.size - 1
                for elem in col:
                    if elem == 1:
                        coords.append(Coordinate(x,y))
                        y += -1
                    else:
                        y += -1
                x += -1

            return coords


        
            

