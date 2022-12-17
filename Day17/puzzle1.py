shapes = [
    [
        [1, 1, 1, 1]
    ],
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    [
        [0, 0, 1],
        [0, 0, 1],
        [1, 1, 1]
    ],
    [
        [1],
        [1],
        [1],
        [1]
    ],
    [
        [1, 1],
        [1, 1]
    ]
]

rowWidth = 7

def addRow(board):
    row = []
    for i in range(rowWidth):
        row.append(0)
    board.append(row)

def ensureRowsUpTo(board, y):
    while y >= len(board):
        addRow(board)
    
def getWidth(shape):
    return len(shape[0])

def getHeight(shape):
    return len(shape)
    
def findBottomMost(shape, relativeX):
    index = getHeight(shape) - 1
    while shape[index][relativeX] == 0:
        index -= 1
        if index < 0:
            print("OOF 3")
            return -999
    return getHeight(shape) - 1 - index

def findLeftMost(shape, relativeY):
    index = 0
    while shape[relativeY][index] == 0:
        index += 1
        if index >= getWidth(shape):
            print("OOF 2")
            return -999
    return index

def findRightMost(shape, relativeY):
    index = getWidth(shape) - 1
    while shape[relativeY][index] == 0:
        index -= 1
        if index < 0:
            print("OOF")
            return -999
    return index

def getVal(board, x, y):
    if x < 0 or x >= rowWidth:
        return 1
    if y >= len(board):
        return 0
    if y < 0:
        return 1
    return board[y][x]

def main():
    file = open("input.txt", "r")
    directions = file.readlines()[0].strip()
    
    board = []
    n = 2022
    shapeIndex = 0
    dirIndex = 0
    
    stopAt = n
    
    i = 1
    while i <= n:
        xPos = 2
        yPos = len(board) + 3
        shape = shapes[shapeIndex]
        width = getWidth(shape)
        height = getHeight(shape)
        done = False
        dirs = []
        while not done:
            # Shift
            direction = directions[dirIndex]
            dirs.append(direction)
            if direction == '>':
                isValid = True
                for relativeY in range(height):
                    x = xPos + findRightMost(shape, relativeY)
                    y = yPos + relativeY
                    if getVal(board, x + 1, y) == 1:
                        isValid = False
                        break
                if isValid:
                    xPos += 1
            elif direction == '<':
                isValid = True
                for relativeY in range(height):
                    x = xPos + findLeftMost(shape, relativeY)
                    y = yPos + relativeY
                    if getVal(board, x - 1, y) == 1:
                        isValid = False
                        break
                if isValid:
                    xPos -= 1
            else:
                print("oof")
                return
            
            # Check if can fall
            onGround = False
            #print("CHECKING ", xPos, yPos)
            for relativeX in range(width):
                x = xPos + relativeX
                y = yPos + findBottomMost(shape, relativeX)
                valBelow = getVal(board, x, y - 1)
                #print(x, y - 1, "->", valBelow)
                if valBelow == 1:
                    onGround = True
                    break
            
            if onGround:
                # Solidify
                done = True
            else:
                # Fall
                yPos -= 1
            
            # Increment
            dirIndex = (dirIndex + 1) % len(directions)
        
        # Place shape
        ensureRowsUpTo(board, yPos + height - 1)
        for yOffset in range(height):
            for xOffset in range(width):
                val = shape[height - yOffset - 1][xOffset]
                if val == 1:
                    board[yPos + yOffset][xPos + xOffset] = 1
        
        # Print board
        if i == stopAt:
            for s in shape:
                print("".join(["#" if r == 1 else " " for r in s]))
            for row in board[::-1]:
                print("|" + "".join(["#" if r == 1 else "." for r in row]) + "|")
            print(xPos, yPos, shapeIndex, len(board))
            
        # Increment
        shapeIndex = (shapeIndex + 1) % len(shapes)
        i += 1
    print(len(board))
    
if __name__ == "__main__":
    main()