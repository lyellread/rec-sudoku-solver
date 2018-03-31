## Sudoku Testing File =

## List: [[5, ' ', 7, ' ', ' ', ' ', ' ', 4, ' '], [' ', 6, ' ', 7, ' ', 8, ' ', ' ', 9], [' ', ' ', 1, ' ', 8, ' ', ' ', ' ', ' '], [' ', 2, ' ', 4, ' ', 5, ' ', 6, ' '], [' ', 7, ' ', 8, ' ', ' ', 9, ' ', ' '], [5, ' ', ' ', 3, ' ', ' ', 2, ' ', 7], [' ', 2, ' ', ' ', 4, ' ', 3, ' ', 9], [9, ' ', 9, ' ', ' ', 6, ' ', 4, ' '], [' ', 6, ' ', 3, 6, 7, 5, 4, 6]]

## Sudoku Basis / Nested Lists / Lyell Read / 3-12-2018

## GRID SETUP / ENTRY ##

import copy

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

## CALCULATION FUNCTIONS ##

def defining_Cell_Values (sudoku_Grid, grid_Row, grid_Column):
    # This function assumes an empty cell at [row][column] and checks the cells that defins what it is, returning a list.
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
    # LATER ;)

    # Flipping Selection (see above)
    temp_List = [x for x in range (1,10)] # 1,2,..8,9
    print(temp_List,defining_List)

    #should use list comp
    for x in defining_List:
        temp_List.remove(x)

    return temp_List # WORKING!!




## PROGRAM BODY - SETUP ##

sudoku_Grid_Clean = grid_Reset(9)
sudoku_Grid_Clean = [[5, ' ', 7, ' ', ' ', ' ', ' ', 4, ' '], [' ', 6, ' ', 7, ' ', 8, ' ', ' ', 9], [' ', ' ', 1, ' ', 8, ' ', ' ', ' ', ' '], [' ', 2, ' ', 4, ' ', 5, ' ', 6, ' '], [' ', 7, ' ', 8, ' ', ' ', 9, ' ', ' '], [5, ' ', ' ', 3, ' ', ' ', 2, ' ', 7], [' ', 2, ' ', ' ', 4, ' ', 3, ' ', 9], [9, ' ', 9, ' ', ' ', 6, ' ', 4, ' '], [' ', 6, ' ', 3, 6, 7, 5, 4, 6]]

## PROGRAM BODY - CALCULATION ##

sudoku_Grid_Guess = copy.deepcopy(sudoku_Grid_Clean)

for grid_Row in range (0,9):
    for grid_Column in range (0,9):
        cell_Guess = defining_Cell_Values(sudoku_Grid_Clean, grid_Row, grid_Column)
        grid_Print(sudoku_Grid_Clean, 9)
        grid_Print(sudoku_Grid_Guess, 9)
        sudoku_Grid_Guess [grid_Row][grid_Column] = cell_Guess

grid_Print (sudoku_Grid_Guess, 9)

#print(sudoku_Grid_Guess)

#make a copy of the knowns after asking if correct
