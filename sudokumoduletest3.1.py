Grid = [[5, ' ', 7, ' ', ' ', ' ', ' ', 4, ' '], [' ', 6, ' ', 7, ' ', 8, ' ', ' ', 9], [' ', ' ', 1, ' ', 8, ' ', ' ', ' ', ' '], [' ', 2, ' ', 4, ' ', 5, ' ', 6, ' '], [' ', 7, ' ', 8, ' ', ' ', 9, ' ', ' '], [5, ' ', ' ', 3, ' ', ' ', 2, ' ', 7], [' ', 2, ' ', ' ', 4, ' ', 3, ' ', 9], [9, ' ', 9, ' ', ' ', 6, ' ', 4, ' '], [' ', 6, ' ', 3, 6, 7, 5, 4, 6]]

corect = [[5, ' ', 7, ' ', 6, ' ', ' ', ' ', 1], [' ', ' ', ' ', 7, ' ', 8, ' ', 8, ' '], [' ', 4, ' ', ' ', ' ', 9, ' ', ' ', ' '], [' ', 2, ' ', ' ', 7, ' ', 5, ' ', ' '], [4, ' ', 5, 8, ' ', ' ', 3, ' ', ' '], [' ', 6, ' ', 9, ' ', ' ', 2, ' ', 7], [' ', 2, ' ', 9, ' ', 9, ' ', 6, ' '], [' ', 4, ' ', ' ', ' ', 6, 3, 6, 7], [3, ' ', 9, ' ', 4, ' ', 5, 4, 6]]

## Define a function that can take each set and turn them into [[box1][box2][box3]]

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

print(translate(Grid))
print ("\n" + str(corect) + "\n\n-----------\n\n")


