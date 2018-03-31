##Grid = [[5, ' ', 7, ' ', ' ', ' ', ' ', 4, ' '], [' ', 6, ' ', 7, ' ', 8, ' ', ' ', 9], [' ', ' ', 1, ' ', 8, ' ', ' ', ' ', ' '], [' ', 2, ' ', 4, ' ', 5, ' ', 6, ' '], [' ', 7, ' ', 8, ' ', ' ', 9, ' ', ' '], [5, ' ', ' ', 3, ' ', ' ', 2, ' ', 7], [' ', 2, ' ', ' ', 4, ' ', 3, ' ', 9], [9, ' ', 9, ' ', ' ', 6, ' ', 4, ' '], [' ', 6, ' ', 3, 6, 7, 5, 4, 6]]

Grid = [[5, ' ', 7, ' ', 6, ' ', ' ', ' ', 1], [' ', ' ', ' ', 7, ' ', 8, ' ', 8, ' '], [' ', 4, ' ', ' ', ' ', 9, ' ', ' ', ' '], [' ', 2, ' ', ' ', 7, ' ', 5, ' ', ' '], [4, ' ', 5, 8, ' ', ' ', 3, ' ', ' '], [' ', 6, ' ', 9, ' ', ' ', 2, ' ', 7], [' ', 2, ' ', 9, ' ', 9, ' ', 6, ' '], [' ', 4, ' ', ' ', ' ', 6, 3, 6, 7], [3, ' ', 9, ' ', 4, ' ', 5, 4, 6]]

Guess = [[[1, 2, 3, 6, 8], [1, 3, 8, 9], [2, 3, 6, 8], [1, 2, 6, 9], [1, 2, 3, 9], [1, 2, 3, 9], [1, 6, 8], [1, 2, 3, 8, 9], [1, 2, 3, 8]], [[1, 2, 3, 4], [1, 3, 4, 5], [2, 3, 4, 5], [1, 2, 5], [1, 2, 3, 5], [1, 2, 3, 4], [1, 4], [1, 2, 3, 5], [1, 2, 3, 4, 5]], [[2, 3, 4, 6, 7], [3, 4, 5, 9], [2, 3, 4, 5, 6], [2, 5, 6, 9], [2, 3, 5, 7, 9], [2, 3, 4, 9], [4, 6, 7], [2, 3, 5, 7, 9], [2, 3, 4, 5]], [[1, 3, 7, 8], [1, 3, 8, 9], [3, 8], [1, 9], [1, 3, 7, 9], [1, 3, 9], [1, 7, 8], [1, 3, 7, 8, 9], [1, 3, 8]], [[1, 2, 3, 4, 6], [1, 3, 4, 5], [2, 3, 4, 5, 6], [1, 2, 5, 6], [1, 2, 3, 5], [1, 2, 3, 4], [1, 4, 6], [1, 2, 3, 5], [1, 2, 3, 4, 5]], [[1, 4, 6, 8], [1, 4, 8, 9], [4, 6, 8], [1, 6, 9], [1, 9], [1, 4, 9], [1, 4, 6, 8], [1, 8, 9], [1, 4, 8]], [[1, 6, 7, 8], [1, 5, 8], [5, 6, 8], [1, 5, 6], [1, 5, 7], [1], [1, 6, 7, 8], [1, 5, 7, 8], [1, 5, 8]], [[1, 2, 3, 7, 8], [1, 3, 5, 8], [2, 3, 5, 8], [1, 2, 5], [1, 2, 3, 5, 7], [1, 2, 3], [1, 7, 8], [1, 2, 3, 5, 7, 8], [1, 2, 3, 5, 8]], [[1, 2, 8], [1, 8, 9], [2, 8], [1, 2, 9], [1, 2, 9], [1, 2, 9], [1, 8], [1, 2, 8, 9], [1, 2, 8]]]

## Break the first three items in the Grid list into a separate one (for testing) and then do the same for the next two:

first_Set = Grid[0:3]
second_Set = Grid[3:6]
third_Set = Grid[6:9]

## Define a function that can take these three sets and turn them into [[box1][box2][box3]]

def to_Box (set):
    temp_Box_1 = []
    temp_Box_2 = []
    temp_Box_3 = []
    for set_Line in set:  ## this iterates for each line of the original List
        temp_Box_1.append(set_Line[0:3])
        temp_Box_2.append(set_Line[3:6])
        temp_Box_3.append(set_Line[6:9])
    return[temp_Box_1,temp_Box_2,temp_Box_3]

## Another function to print these lists... just to make understanding easier

def grid_Print (sudoku_Grid, side_Length):
    print("|---|---|---|---|---|---|---|---|---|")
    for grid_Row in range (0,side_Length):
        print("| ", end="")
        for grid_Column in range (0,side_Length):
            print (str(sudoku_Grid [grid_Row][grid_Column]), end=" | ")
        print("\n|---|---|---|---|---|---|---|---|---|")

grid_Print (Grid, 9)

grid_Out = []

temp_List = []
for x in to_Box (first_Set):
    for y in x:
        for z in y:
            temp_List.append(z)
    grid_Out.append(temp_List)
    temp_List = []

for x in to_Box (second_Set):
    for y in x:
        for z in y:
            temp_List.append(z)
    grid_Out.append(temp_List)
    temp_List = []

for x in to_Box (third_Set):
    for y in x:
        for z in y:
            temp_List.append(z)
    grid_Out.append(temp_List)
    temp_List = []

grid_Print (grid_Out,9)



