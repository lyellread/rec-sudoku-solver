import copy

def singleton_Input (sudoku_Grid, sudoku_Guess):
    for x in range (0,9):
        for y in range (0,9):
            if len(sudoku_Guess [x][y]) == 1 and not sudoku_Guess[x][y] == "X" :
                sudoku_Grid [x][y] = sudoku_Guess[x][y][0]
    return sudoku_Grid


def grid_Print (sudoku_Grid, side_Length):
    print("|---|---|---|---|---|---|---|---|---|")
    for grid_Row in range (0,side_Length):
        print("| ", end="")
        for grid_Column in range (0,side_Length):
            print (str(sudoku_Grid [grid_Row][grid_Column]), end=" | ")
        print("\n|---|---|---|---|---|---|---|---|---|")

        
sudoku_Grid_Clean = [[' ', 1, 7, ' ', ' ', ' ', 4, ' ', ' '],
                    [' ', 2, 9, ' ', ' ', 6, 3, ' ', 1],
                    [' ', ' ', 4, ' ', 1, ' ', 5, ' ', 7],
                    [7, ' ', 2, ' ', ' ', 1, ' ', 5, 4],
                    [4, 5, 3, ' ', 9, ' ', 2, 1, ' '],
                    [' ', ' ', 1, ' ', ' ', 5, ' ', 7, 3],
                    [2, 7, 6, 1, ' ', 4, ' ', ' ', 5],
                    [9, 3, 5, ' ', 6, ' ', ' ', 4, 2],
                    [1, 4, 8, ' ', 5, 2, ' ', ' ', ' ']
                    ]

sudoku_Guess = [[[8, 3, 5, 6], 'X', 'X', [2, 3, 5, 8, 9], [8, 2, 3], [8, 9, 3], 'X', [8, 9, 2, 6], [8, 9, 6]],
                [[8, 5], 'X', 'X', [8, 4, 5, 7], [8, 4, 7], 'X', 'X', [8], 'X'],
                [[8, 3, 6], [8, 6], 'X', [8, 9, 2, 3], 'X', [8, 9, 3], 'X', [8, 9, 2, 6], 'X'],
                ['X', [8, 9, 6], 'X', [8, 3, 6], [8, 3], 'X', [8, 9, 6], 'X', 'X'],
                ['X', 'X', 'X', [8, 6, 7], 'X', [8, 7], 'X', 'X', [8, 6]],
                [[8, 6], [8, 9, 6], 'X', [8, 2, 4, 6], [8, 2, 4], 'X', [8, 9, 6], 'X', 'X'],
                ['X', 'X', 'X', 'X', [8, 3], 'X', [8, 9], [8, 9, 3], 'X'],
                ['X', 'X', 'X', [8, 7], 'X', [8, 7], [8, 1, 7], 'X', 'X'],
                ['X', 'X', 'X', [9, 3, 7], 'X', 'X', [9, 6, 7], [9, 3, 6], [9, 6]]]

for x in range (0,9):
    for y in range (0,9):
        if not sudoku_Guess [x][y] == "X":
            print(sudoku_Guess [x][y])
            for z in sudoku_Guess [x][y]:
                #copy; substitute; theoretical rerun -
                attempt_list = copy.deepcopy(sudoku_Grid_Clean)
                attempt_list [x][y] = z
                #grid_Print (attempt_list,9)
print(attempt_list)

#print(sudoku_Guess)
#grid_Print(sudoku_Grid_Clean,9)
#grid_Print(singleton_Input(sudoku_Grid_Clean, sudoku_Guess),9)
