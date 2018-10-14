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
