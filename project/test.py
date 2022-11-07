#Imports
from objects.grid import Grid

try:
    #grid = Grid([0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0])
    grid = Grid([1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1])

    #print(grid.get_inputs())
    #print(grid.get_num_elements())
    #print(grid.get_size())
    #print(grid.get_rows())
    #print(grid.get_columns())

    print("Row coords with blocks")
    display_row_commands = grid.get_coords("row")
    for coord in display_row_commands:
        coord.__repr__()

    print("Col coords with blocks")
    display_col_commands = grid.get_coords("col")
    for coord in display_col_commands:
        coord.__repr__()

except BaseException as error:
    print(error)

