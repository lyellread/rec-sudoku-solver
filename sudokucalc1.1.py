## Sudoku Basis / Nested Lists / Lyell Read / 3-12-2018

import copy

## GRID SETUP / ENTRY ##

def grid_Reset (side_Length):
    sudoku_Grid = []
    for grid_Row in range (0,side_Length):
        sudoku_Grid.append([0,0,0,0,0,0,0,0,0])
    return (sudoku_Grid)


def grid_Print (sudoku_Grid, side_Length):
    print("|---|---|---|---|---|---|---|---|---|")
    for grid_Row in range (0,side_Length):
        print("| ", end="")
        for grid_Column in range (0,side_Length):
            print (str(sudoku_Grid [grid_Row][grid_Column]), end=" | ")
        print("\n|---|---|---|---|---|---|---|---|---|")

def grid_Populate (sudoku_Grid, side_Length):
    for grid_Row in range (0,side_Length):
        for grid_Column in range (0,side_Length):
            temp_Entry = input("Enter the value for row #" + str(grid_Row +1) + ", column #" + str(grid_Column +1) + ":")
            while not temp_Entry in ["1","2","3","4","5","6","7","8","9","",".","-"," "]:
               temp_Entry = input("Try Again (not in range): ")
            if temp_Entry == "" or temp_Entry == " " or temp_Entry == "." or temp_Entry == "-":
                sudoku_Grid [grid_Row] [grid_Column] = " "
            else:
                sudoku_Grid [grid_Row] [grid_Column] = int(temp_Entry)
    return (sudoku_Grid)

def cell_Populate (sudoku_Grid):
    grid_Row = int(input("Enter row number:"))-1
    grid_Column = int(input("Enter column number:"))-1

    cell_Entry = input("The current value for that cell: " + str(sudoku_Grid [grid_Row] [grid_Column]) + "; Change to :")
    while not cell_Entry in ["1","2","3","4","5","6","7","8","9","",".","-"," "]:
               cell_Entry = input("Try Again (not in range): ")
    if cell_Entry == "" or cell_Entry == " " or cell_Entry == "." or cell_Entry == "-":
        sudoku_Grid [grid_Row] [grid_Column] = " "
    else:
        sudoku_Grid [grid_Row] [grid_Column] = int(cell_Entry)

    return (sudoku_Grid)

## CALCULATION FUNCTIONS ##

def defining_Cell_Values (sudoku_Grid, grid_Row, grid_Column):
    # This finction assumes an empty cell at [row][column] and checks the cells that defins what it is, returning a list.
    # Operation in three parts: defining row, defining column, and defmining square (3X3).
    # Then it returns the inverse of that list (i.e. [1,2,5,6,9] are in the defining spaces, then returns [3,4,7,8] as possible values for that cell)

    defining_List = []
    temp_List = []

    # Defnining Row / working
    temp_List = sudoku_Grid [grid_Row]
    for x in temp_List:
        if not x in defining_List and not x == " ":
            defining_List.append(x)
    # Defining Column / working
    temp_List = [item[grid_Column] for item in sudoku_Grid]
    for x in temp_List:
        if not x in defining_List and not x == " ":
            defining_List.append(x)

    # Defnining square

    # Process: remake the sudoku_Grid_Guess in the form of 

    # Flipping Selection (see above)
    temp_List = [x for x in range (1,10)] # 1,2,..8,9

    #should use list comp
    for x in defining_List:
        temp_List.remove(x)

    return temp_List # WORKING!!




## PROGRAM BODY - SETUP ##

sudoku_Grid_Clean = grid_Reset(9)
choice_Entry = 1
while not choice_Entry == 4:
    choice_Entry = int(input("NOTE: enter '.','',' ',or '-' to enter a blank cell\n\nWhat to do:\n1 - print table\n2 - replace an individual value\n3 - enter all values\n4 - exit\n\nChoice   :"))
    if choice_Entry == 1:
        grid_Print(sudoku_Grid_Clean, 9)
    elif choice_Entry == 2:
        sudoku_Grid_Clean = cell_Populate(sudoku_Grid_Clean)
    elif choice_Entry == 3:
        sudoku_Grid_Clean = grid_Populate(sudoku_Grid_Clean, 9)
        print (sudoku_Grid_Clean)

## PROGRAM BODY - CALCULATION ##
########
sudoku_Grid_Clean = [[5, ' ', 7, ' ', ' ', ' ', ' ', 4, ' '], [' ', 6, ' ', 7, ' ', 8, ' ', ' ', 9], [' ', ' ', 1, ' ', 8, ' ', ' ', ' ', ' '], [' ', 2, ' ', 4, ' ', 5, ' ', 6, ' '], [' ', 7, ' ', 8, ' ', ' ', 9, ' ', ' '], [5, ' ', ' ', 3, ' ', ' ', 2, ' ', 7], [' ', 2, ' ', ' ', 4, ' ', 3, ' ', 9], [9, ' ', 9, ' ', ' ', 6, ' ', 4, ' '], [' ', 6, ' ', 3, 6, 7, 5, 4, 6]]
########
sudoku_Grid_Guess = copy.deepcopy(sudoku_Grid_Clean)

for grid_Row in range (0,9):
    for grid_Column in range (0,9):
        cell_Guess = defining_Cell_Values(sudoku_Grid_Clean, grid_Row, grid_Column)
        #grid_Print(sudoku_Grid_Clean, 9)
        #grid_Print(sudoku_Grid_Guess, 9)
        sudoku_Grid_Guess [grid_Row][grid_Column] = cell_Guess

print ("\n\n" + str(sudoku_Grid_Guess))

#print(sudoku_Grid_Guess)

#make a copy of the knowns after asking if correct
