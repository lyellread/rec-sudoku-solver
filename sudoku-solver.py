## Sudoku Solver
## Lyell Read 9.2.2018

import analysis
import sudokuio
import edit

#starter input

grid=sudokuio.grid_entry(edit.clear())


breakout = False #set to true to break the while and continue on to deep guessing (BETA)
while breakout == False and analysis.solved(grid) == False:
    guess = analysis.guess_all(grid)
    if analysis.valid_guess(guess) == True:
        grid=analysis.guess_substitute(grid,guess)
    else:
        breakout=True

if breakout == True:
    print ("DEEP+GUESS+BETA")
else:
    print("YAY! I solved your puzzle. Here's what I got:\n")
    sudokuio.print_grid(grid)
