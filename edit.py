## Sudoku Modules involving the modification of the grid
## Part of the Sudoku Solver. Lyell Read. 9.2.2" "18

#[clear] - return clear 9X9 grid

def clear ():
    grid = []
    for grid_Row in range (0,9):
        grid.append([" "," "," "," "," "," "," "," "," "])
    return (grid)

#[translate] - switch between BOX and STD formats of the list

def to_Box (chunk):
    temp_Box_1 = []
    temp_Box_2 = []
    temp_Box_3 = []
    for set_Line in chunk:  ## this iterates for each line of the original List
        temp_Box_1.append(set_Line[0:3])
        temp_Box_2.append(set_Line[3:6])
        temp_Box_3.append(set_Line[6:9])
    return[temp_Box_1,temp_Box_2,temp_Box_3]

def translate(grid):
    grid_Out = []
    for index in range (0,3): # will have to add one to compensate for the weidr indexing
        active_Set = grid[(index*3):((index+1)*3)]
        temp_List = []
        for x in to_Box(active_Set):
            for y in x:
                for z in y:
                    temp_List.append(z)
            grid_Out.append(temp_List)
            temp_List = []
    return (grid_Out)

