
class Coordinate:
    #Constructor
    def __init__(self,x_coord,y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
    
    #Returns the x_pos
    def get_x(self):
        return self.x_coord

    #Returns the y_pos
    def get_y(self):
        return self.y_coord

    #Outputs coords in string format
    def __repr__(self):
        print((self.x_coord,self.y_coord))
    
