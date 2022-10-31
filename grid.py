import math
import copy

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
    
    def __repr__(self):
        return ""
