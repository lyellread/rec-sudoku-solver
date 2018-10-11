## Sudoku Modules involving I/O tasks
## Part of the Sudoku Solver. Lyell Read. 9.2.2018

#[input_full] - Full input (fill a whole 9X9 grid)

def input_full(grid):
    print ("Entry Instructions: Enter the number that corresponds to the cell requested. just hit return to enter a blank cell.\n\n")
    for grid_Row in range (0,9):
        for grid_Column in range (0,9):
            temp_Entry = input("Enter the value for row #" + str(grid_Row +1) + ", column #" + str(grid_Column +1) + ":")
            while not temp_Entry in ["1","2","3","4","5","6","7","8","9",""]:
               temp_Entry = input("Error: input not in acceptable range: ")
            if temp_Entry == "": #this is an empty cell. We'll have to solve for it :)
                grid [grid_Row] [grid_Column] = " " #Empty cell is entered as a space.
            else:
                #If the entry is not an empty cell, let's make the entry an integer, as we know it is.
                grid [grid_Row] [grid_Column] = int(temp_Entry)
    return (grid)

#[input_single] - Fill single (put a value in a spot, with correct indexing, or blank that spot)

def input_single(grid):
    grid_Row = int(input("Enter row number:"))-1
    grid_Column = int(input("Enter column number:"))-1
    print("\nNote: Press the return key to enter a blank cell\n")
    cell_Entry = input("The current value for that cell: " + str(grid [grid_Row] [grid_Column]) + "; Change to :")
    while not cell_Entry in ["1","2","3","4","5","6","7","8","9",""]:
        cell_Entry = input("Error: input not in acceptable range: ")
    if cell_Entry == "":
        grid [grid_Row] [grid_Column] = " "
    else:
        grid [grid_Row] [grid_Column] = int(cell_Entry)

    return (grid)

#[print_grid] - Print out grid in a neat way

def print_grid(grid):
    print("|---|---|---|---|---|---|---|---|---|")
    for grid_Row in range (0,9):
        print("| ", end="")
        for grid_Column in range (0,9):
            print (str(grid [grid_Row][grid_Column]), end=" | ")
        print("\n|---|---|---|---|---|---|---|---|---|")
    return 0

def grid_entry (grid):
    print ("Welcome to the Sudoku Solver.\nNote: `Deep Guessing` not supported at this time")

    grid=input_full(grid)
    print_grid(grid)
    ok = input("Does this grid look groovy, baby? (Y|N) :")
    while not ok.upper() == "Y":
        if ok.upper() == "N":
            print("I think you're looking to change an individual digit. Let's do that!")
            grid=input_single (grid)
            print_grid(grid)
            ok = input("Looks good now? :")
        else:
            ok=input("Bad Input. Try Again:")
    print (grid)
    return grid
