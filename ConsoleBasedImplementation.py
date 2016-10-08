import random


def printGrid(Grid):
    """Prints the argument list in 4 x 4 grid."""
    for i in range(4):
        print(str(Grid[i]), end=" ")
    print("")
    for i in range(4, 8):
        print(str(Grid[i]), end=" ")
    print("")
    for i in range(8, 12):
        print(str(Grid[i]), end=" ")
    print("")
    for i in range(12, 16):
        print(str(Grid[i]), end=" ")
    print("")


def gravity(Grid):
    """Pulls a number down if there is zero beneath it."""
    for i in range(16):
        if i == 12 or i == 13 or i == 14 or i == 15:
            continue
        elif Grid[i] != 0 and Grid[i + 4] == 0:
            Grid[i + 4] = Grid[i]
            Grid[i] = 0
    return Grid


def moveDown(Grid):
    """Handles move down logic of 2048.
    Returns a modified list."""
    Grid = gravity(Grid)
    Grid = gravity(Grid)
    Grid = gravity(Grid)
    for i in range(0, 16):
        if i == 12 or i == 13 or i == 14 or i == 15:
            continue
        elif Grid[i] == Grid[i + 4] and Grid[i] != 0:
            Grid[i] = Grid[i] * 2
            Grid[i + 4] = 0
        # Conditional to handle the problem casses
        elif i < 4 and Grid[i + 4] == Grid[i + 8] and Grid[i + 8] == Grid[i + 12]:
            for l in range(4):
                if Grid[i + 4] == Grid[i + 8] and Grid[i + 8] == Grid[i + 12] and Grid[i + 8] == Grid[i + 12]:
                    Grid[i + 8] = Grid[i + 12] * 2
                    Grid[i + 12] = 0
    Grid = gravity(Grid)
    Grid = gravity(Grid)
    Grid = gravity(Grid)
    return Grid


def rotate_90(temp_list):
    """Returns a 90 degree rotated list."""
    rotated_list = [0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0]
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


def move(direction, Grid):
    """Performs the movement based on the provided arguments.
    Returns a list with the new modifications."""
    if direction == "u":
        Grid = rotate_90(Grid)
        Grid = rotate_90(Grid)
        Grid = moveDown(Grid)
        Grid = rotate_90(Grid)
        Grid = rotate_90(Grid)
        return Grid
    elif direction == "d":
        Grid = moveDown(Grid)
        return Grid
    elif direction == "l":
        Grid = rotate_90(Grid)
        Grid = rotate_90(Grid)
        Grid = rotate_90(Grid)
        Grid = moveDown(Grid)
        Grid = rotate_90(Grid)
        return Grid
    elif direction == "r":
        Grid = rotate_90(Grid)
        Grid = moveDown(Grid)
        Grid = rotate_90(Grid)
        Grid = rotate_90(Grid)
        Grid = rotate_90(Grid)
        return Grid


def randomNums():
    """Returns a list of two unique random numbers.
    Random numbers range from 0 - 15 (inclusive)."""
    while True:
        randVar1 = random.randint(0, 15)
        randVar2 = random.randint(0, 15)
        if randVar2 != randVar1:
            return [randVar1, randVar2]


def initBoard(Grid):
    """Initialize the board by add '2' at random positions in the Grid.
    Returns the modified list."""
    rand_list = randomNums()
    randVar1 = rand_list[0]
    randVar2 = rand_list[1]
    Grid[randVar1] = 2
    Grid[randVar2] = 2
    return Grid


def addRandtwo(Grid):
    """Returns a list with '2' randomly at any '0' in the Grid."""
    tempList = []
    for i in range(16):
        if Grid[i] == 0:
            tempList.append(i)
    if tempList == []:
        return Grid
    a = random.choice(tempList)
    Grid[a] = 2
    return Grid


def getInput():
    """Returns legal input directions."""
    while True:
        i1 = input("Input direction : ")
        i1 = i1.lower()
        if i1 == "u" or i1 == "l" or i1 == "r" or i1 == "d":
            return i1
        else:
            print("Invalid Input!!!")


def checkWin(Grid):
    """Returns 'lose' if no move is possible."""
    for i in range(16):
        if Grid[i] == 0:
            return
    tempList = Grid[:]
    tempList = move("u", tempList)
    tempList = move("d", tempList)
    tempList = move("l", tempList)
    tempList = move("r", tempList)
    if Grid == tempList:
        return "lose"


def gameLoop():
    """Runs the console based implemetation of the game."""
    Grid = [0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0]
    Grid = initBoard(Grid)
    gameRun = True
    while gameRun == True:
        printGrid(Grid)
        userInput = getInput()
        Grid = move(userInput, Grid)
        state = checkWin(Grid)
        Grid = addRandtwo(Grid)
        if state == "win":
            print("You win!!!")
            return
        elif state == "lose":
            print("You lose")
            return


if __name__ == "__main__":
    gameLoop()
