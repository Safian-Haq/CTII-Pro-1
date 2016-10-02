#Main Grid
Grid = [0,0,0,0,
        0,0,0,0,
        0,0,0,0,
        0,0,0,0]

def printGrid():
    global Grid
    for i in range(4):
        for j in range(4):
            print(str(Grid[j+i]) + "  ", end="")
        print("")


def moveUp():
    global Grid
    for i in range(Grid):
        if i == 0 or i == 1 or i == 2 or i == 3:
            continue
        #elif Grid[]

def check_win():
    global Grid
    sum = 0
    zero_counter = 0
    for i in range(9):
        sum = sum + Grid[i]
        if Grid[i] == 0:
            zero_counter += 1
    if sum >= 2048:
        print ("You Win !!!")
        return "win"
    elif zero_counter == 0:
        print ("You Lost")
        return "lose"

def rotate_90(temp_list):
    rotated_list = [0,0,0,0,
                    0,0,0,0,
                    0,0,0,0,
                    0,0,0,0]
    rotated_list[0] = temp_list[12]
    rotated_list[1] = temp_list[8]
    rotated_list[2] = temp_list[4]
    rotated_list[3] = temp_list[0]
    rotated_list[4] = temp_list[13]
    rotated_list[5] = temp_list[9]
    rotated_list[6] = temp_list[5]
    rotated_list[7] = temp_list[1]
    rotated_list[8] = temp_list[14]
    rotated_list[9] = temp_list[10]
    rotated_list[10] = temp_list[6]
    rotated_list[11] = temp_list[2]
    rotated_list[12] = temp_list[15]
    rotated_list[13] = temp_list[11]
    rotated_list[14] = temp_list[7]
    rotated_list[15] = temp_list[3]
    return rotated_list

def rotate(direction, Grid_list):
    rotated_list = [0,0,0,0,
                    0,0,0,0,
                    0,0,0,0,
                    0,0,0,0]
    if direction == "l":
        rotated_list = rotate_90(Grid_list)
    elif direction == "d":
        rotated_list = rotate_90(Grid_list)
        rotated_list = rotate_90(rotated_list)
    elif direction == "r":
        rotated_list = rotate_90(Grid_list)
        rotated_list = rotate_90(rotated_list)
        rotated_list = rotate_90(rotated_list)

    return rotated_list



def move(direction):
    while True:
        if direction == "u":
            pass
            break
        elif direction == "d":
            pass
            break
        elif direction == "l":
            pass
            break
        elif direction == "r":
            pass
            break
        else:
            print("Invalid Input")

Test = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(rotate_90(Test))
print(rotate("r",Test))

printGrid()