## Sudoku Modules involving the analysis of the grid
## Part of the Sudoku Solver. Lyell Read. 9.2.2018

## Notes: I've decided (arbitrarily, granted) to use the three (row, column and square) eclusions/checks/defining-values on a cell-wise basis, and then to run many times... As usual with anyting I decide, the altherlative is probably better and more correct, but at this point I couldn't care.

import edit

#[guess_cell] - Generate guesses for a certain cell. Combines row, column

def guess_cell_rc (grid, row, column):

    return(list(set(guess_rc("row",grid, row,column))&set(guess_rc("column",grid, row,column))))

#[guess_rc] - returns the possible values for a cell based on either row or column (specified by the `toggle` argument)

def guess_rc (toggle, grid, row, column):

    output = [] # this will store all the output, pre and post flip.... read on ;)
    if toggle == "row":
        temp = grid [row] #set temp to be the whole row
    if toggle == "column":
        temp = [item[column] for item in grid]
    for item in temp:
        if not item == " ": #provided that each cell of the row isn't a blank, add it to the output list
            output.append(item)
    output=[value for value in [x for x in range (1,10)] if value not in output] # holy listcomp Batman! All this does is sets output to all the numbers in 1..9 that aren't in output already, thus "inverting selection" as I like to think about it.
    return output #Tested. Seems to work OK :)

#[guess_box] - Returns all possible values for a cell based only on the Box it is part of.

def guess_box (grid, guess):

    #ENTERING THE SQUARE ZONE
    grid_square = edit.translate(grid)
    guess_square = edit.translate(guess)

    for box in range (0,9):
        for item in range (0,9):
            if grid_square[box][item] == " ":
                guess_square[box][item] = guess_rc("row", grid_square, box, None) #columns dont matter in square world, but the guess_rc fxn can be used to check the box which has become a row...

    #LEAVING THE SQUARE ZONE
    guess = edit.translate(guess_square)

    return guess
#[solved] - Returns T/F if grid solved or not

def solved (grid):
    for row in grid:
        for cell in row:
            if cell == " ": #for every single cell in the grid (NOT the guess grid...) check to make sure that there is a number there and not the " " that indicates no value found yet.
                return False
    return True

#[valid_guess] - Returns T/F if there is a guess that has only one element (the definitive answer for a cell)

def valid_guess (guess):
    for row in guess:
        for cell in row:
            if len(cell) == 1: #check that guess length is 1 indicating a correct guess.
                return True
    return False

# [any_guess] - returns T if there are any available guesses, false if the grid is a dead end.

def any_guess (guess):
    for row in guess:
        for cell in row:
            if len(cell) >= 1: #check that guess length is greater than or equal to 1 which indicates presence of guesses.
                return True
    return False

#[guess_substitute] - replaces empty cells if there is a valid guess for that cell

def guess_substitute (grid, guess):
    for row in range (0,9):
        for column in range (0,9):
            if len(guess[row][column]) == 1 and grid[row][column] == " ":
                grid[row][column] = guess [row] [column][0] #if there is only one guess, substitute it. Zero is there to make sure that it is entered as "#" and not "[#]"
                print("Guess in cell (" + str(row+1) + "," + str(column+1)+") adopted into official grid with value " + str(guess [row] [column][0]) + ".")
    return grid

#[guess_all] - runs guess_cell on all cells
def guess_all(grid):
    print ("Guessing Sequence Initiated")
    sq_guess = guess_box(grid, edit.clear()) #generate the guesses for every square with respect to the square

    for column in range (0,9):
        for row in range (0,9):
            sq_guess [row][column] = list(set(sq_guess [row][column]) & set(guess_cell_rc(grid, row,column))) #as I progress through sq_guess, I merge it with the individually generated cell guess with respect to row and column.
    return sq_guess
