## Sudoku Solver, Non-Guess Module

import analysis
import sudokuio
import edit


grid=sudokuio.grid_entry(edit.clear())

#grid=[[' ', ' ', 2, 6, ' ', 4, ' ', 9, 3],
#        [' ', 6, ' ', ' ', 2, ' ', 4, ' ', ' '],
#        [5, ' ', 4, ' ', ' ', 7, ' ', ' ', ' '],
#        [2, ' ', 3, ' ', ' ', ' ', ' ', ' ', ' '],
#        [' ', ' ', 8, ' ', ' ', ' ', 6, ' ', ' '],
#        [' ', ' ', ' ', ' ', ' ', ' ', 1, ' ', 8],
#        [' ', ' ', ' ', 3, ' ', ' ', 7, ' ', 5],
#        [' ', ' ', 7, ' ', 4, ' ', ' ', 2, ' '],
#        [8, 2, ' ', 9, ' ', 6, 3, ' ', ' ']]

def next_cell (grid, row, col):
    for x in range (row, 9):
        for y in range (col, 9):
            if grid [x][y] == ' ':
                return x,y
    for x in range (0,9):
        for y in range (0,9):
            if grid [x][y] == ' ':
                return x,y
    return -1, -1

def valid (grid, row, col, value):
    sq_guess = analysis.guess_box(grid, edit.clear())
    possible_entries = list(set(sq_guess [row][col]) & set(analysis.guess_cell_rc(grid, row, col)))

    if value in possible_entries:
        return True
    return False

def solve (grid, row=0, col=0):
    row, col = next_cell (grid, row, col)
    if row == -1:
        return True
    for test_value in range (1,10):
        if valid (grid, row, col, test_value):
            grid [row][col] = test_value
            if solve(grid, row, col):
                return True
            grid [row][col] = ' '
    return False

if solve(grid):
    print(grid)
    quit()
print("ERROR")
quit()
