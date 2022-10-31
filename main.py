from grid import Grid

try:
    #grid = Grid([0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0])
    grid = Grid([1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1])

    #print(grid.get_inputs())
    #print(grid.get_num_elements())
    #print(grid.get_size())
    #print(grid.get_rows())
    #print(grid.get_columns())
    grid.__repr__()

    
    
except BaseException as error:
    print(error)

