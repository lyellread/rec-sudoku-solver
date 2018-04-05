## Sudoku Basis / Nested Lists / Lyell Read / 3-12-2018


#sudoku_Grid = []

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
            if temp_Entry == "" or temp_Entry == " " or temp_Entry == "." or temp_Entry == "-":
                sudoku_Grid [grid_Row] [grid_Column] = " "
            else:
                sudoku_Grid [grid_Row] [grid_Column] = int(temp_Entry)
    return (sudoku_Grid)

def cell_Populate (sudoku_Grid):
    grid_Row = int(input("Enter row number:"))-1
    grid_Column = int(input("Enter column number:"))-1

    cell_Entry = input("The current value for that cell: " + str(sudoku_Grid [grid_Row] [grid_Column]) + "; Change to :")
                      
    if cell_Entry == "" or cell_Entry == " " or cell_Entry == "." or cell_Entry == "-":
        sudoku_Grid [grid_Row] [grid_Column] = " "
    else:
        sudoku_Grid [grid_Row] [grid_Column] = int(cell_Entry)

    return (sudoku_Grid)



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
