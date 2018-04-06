## Sudoku Calc / Nested Lists / Lyell Read / 3-12-2018

import copy

## ---------- GRID SETUP / ENTRY ---------- ##

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

## ---------- GRID MANIPULATION TOOLS ---------- ##

def to_Box (set):
    temp_Box_1 = []
    temp_Box_2 = []
    temp_Box_3 = []
    for set_Line in set:  ## this iterates for each line of the original List
        temp_Box_1.append(set_Line[0:3])
        temp_Box_2.append(set_Line[3:6])
        temp_Box_3.append(set_Line[6:9])
    return[temp_Box_1,temp_Box_2,temp_Box_3]

def translate(Grid):
    grid_Out = []
    for index in range (0,3): # will have to add one to compensate for the weidr indexing
        active_Set = Grid[(index*3):((index+1)*3)]

        ## gotta get the formatting of the output list right

        temp_List = []
        for x in to_Box(active_Set):
            for y in x:
                for z in y:
                    temp_List.append(z)
            grid_Out.append(temp_List)
            temp_List = []
    return (grid_Out)

## ---------- CALCULATION FUNCTIONS ---------- ##

def defining_Cell_Values (sudoku_Grid, grid_Row, grid_Column):

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


    # Flipping Selection (see above)
    temp_List = [x for x in range (1,10)] # 1,2,..8,9

    #should use list comp
    for x in defining_List:
        temp_List.remove(x)

    return temp_List # WORKING!!

def defining_Square_Values (sudoku_Grid, sudoku_Guess):
    ## Entering the square zone
    sudoku_Grid = translate(sudoku_Grid)
    sudoku_Guess = translate(sudoku_Guess)

    for square in range (0,9):
        for item in range (0,9):
        #defining_List = []
            temp_List = [x for x in sudoku_Grid[square] if not x == ' ']
            temp_List = list(set(temp_List))
            if sudoku_Grid [square][item] == " ":
                defining_List = [x for x in range (1,10)] # 1,2,..8,9
                for x in temp_List:
                        defining_List.remove(x)
                sudoku_Guess [square][item] = defining_List
            else:
                sudoku_Guess [square][item] = "X" # fill knowns with x to make new certain values easy to find...
    # Exiting the square zone
    sudoku_Grid = translate(sudoku_Grid)
    sudoku_Guess = translate(sudoku_Guess)

    return sudoku_Guess

def overlap (list1, list2):
    output_List = grid_Reset (9)
    for row in range(0,9):
        for column in range(0,9):
            if not list1 [row][column] == "X":
                output_List [row][column] = list (set(list1 [row][column]) & set(list2[row][column]))
            else:
                output_List [row][column] = "X"
    return output_List

def generate_Guess (sudoku_Grid_Clean):
    sudoku_Grid_Guess_SQ = copy.deepcopy(sudoku_Grid_Clean)
    sudoku_Grid_Guess_HV = copy.deepcopy(sudoku_Grid_Clean)

    sudoku_Grid_Guess_SQ = defining_Square_Values (sudoku_Grid_Clean, sudoku_Grid_Guess_SQ)

    for row in range (0,9):
        for column in range (0,9):
            if sudoku_Grid_Clean [row][column] == " ":
                sudoku_Grid_Guess_HV [row][column] = defining_Cell_Values (sudoku_Grid_Clean, row, column)
            else:
                sudoku_Grid_Guess_HV [row][column] = "X"

    sudoku_Grid_Guess = overlap(sudoku_Grid_Guess_HV, sudoku_Grid_Guess_SQ)
    return sudoku_Grid_Guess

def singleton_Input (sudoku_Grid, sudoku_Guess):
    for x in range (0,9):
        for y in range (0,9):
            if len(sudoku_Guess [x][y]) == 1 and not sudoku_Guess[x][y] == "X" :
                sudoku_Grid [x][y] = sudoku_Guess[x][y][0]
    return sudoku_Guess

def begin_Check (sudoku_Grid):
    sudoku_Guess = generate_Guess(sudoku_Grid)

    singleton_Input(sudoku_Grid, sudoku_Guess)

    if [] in sudoku_Guess: # Broken branch - must quit
        print( "Broken Branch - Quitting" )

    return False

    elif len(max(sudoku_Guess, key=len)) == 1: ##Solved!!!
        print("Solved!")
        grid_Print(sudoku_Grid)
        global answer_Grid = sudoku_Grid
        return True

    else:
        #for each possible guess
	    #deepcopy the sudoku list
        # alter that sudoku list deepcopy
	    #do function with that guess list


## ---------- PROGRAM BODY - INPUT ---------- ##

answer_Grid = []

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

## ---------- PROGRAM BODY - CALCULATION ---------- ##
########
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

#sudoku_Guess = [[[8, 3, 5, 6], 'X', 'X', [2, 3, 5, 8, 9], [8, 2, 3], [8, 9, 3], 'X', [8, 9, 2, 6], [8, 9, 6]],
#                [[8, 5], 'X', 'X', [8, 4, 5, 7], [8, 4, 7], 'X', 'X', [8], 'X'],
#                [[8, 3, 6], [8, 6], 'X', [8, 9, 2, 3], 'X', [8, 9, 3], 'X', [8, 9, 2, 6], 'X'],
#                ['X', [8, 9, 6], 'X', [8, 3, 6], [8, 3], 'X', [8, 9, 6], 'X', 'X'],
#                ['X', 'X', 'X', [8, 6, 7], 'X', [8, 7], 'X', 'X', [8, 6]],
#                [[8, 6], [8, 9, 6], 'X', [8, 2, 4, 6], [8, 2, 4], 'X', [8, 9, 6], 'X', 'X'],
#                ['X', 'X', 'X', 'X', [8, 3], 'X', [8, 9], [8, 9, 3], 'X'],
#                ['X', 'X', 'X', [8, 7], 'X', [8, 7], [8, 1, 7], 'X', 'X'],
#                ['X', 'X', 'X', [9, 3, 7], 'X', 'X', [9, 6, 7], [9, 3, 6], [9, 6]]
#

                ]
########
sudoku_Grid_Guess = generate_Guess(sudoku_Grid_Clean)

#print ([] in sudoku_Grid_Guess)












# just to have spare lines ;)
