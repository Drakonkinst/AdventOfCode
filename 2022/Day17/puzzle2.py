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
            assert False
    return getHeight(shape) - 1 - index

def findLeftMost(shape, relativeY):
    index = 0
    while shape[getHeight(shape) - relativeY - 1][index] == 0:
        index += 1
        if index >= getWidth(shape):
            assert False
    return index

def findRightMost(shape, relativeY):
    index = getWidth(shape) - 1
    while shape[getHeight(shape) - relativeY - 1][index] == 0:
        index -= 1
        if index < 0:
            assert False
    return index

def getVal(board, x, y):
    if x < 0 or x >= rowWidth:
        return 1
    if y >= len(board):
        return 0
    if y < 0:
        return 1
    return board[y][x]
    
def rowToNumber(row):
    total = 0
    exp = 0
    for x in row:
        if x == 1:
            total += 2 ** exp
        exp += 1
    return total

def compressRowNumbers(rowNums):
    total = 0
    for x in rowNums:
        total = (total << 7) + x
    return total

def getLastXRows(board, x):
    lastXRows = []
    for i in range(x):
        index = len(board) - 1 - i
        if index < 0:
            lastXRows.append(0)
        else:
            lastXRows.append(rowToNumber(board[index]))
    return lastXRows

def main():
    file = open("input.txt", "r")
    directions = file.readlines()[0].strip()
    
    board = []
    n = 1000000000000
    dirIndex = 0
    
    numRowsToSave = 5
    seenStates = {}
    cycleBonus = 0
    
    stopAt = n
    
    i = 0
    while i < n:
        xPos = 2
        yPos = len(board) + 3
        shapeNum = i + 1
        shapeIndex = i % len(shapes)
        shape = shapes[shapeIndex]
        width = getWidth(shape)
        height = getHeight(shape)
        done = False
        dirs = []
        valids = []
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
                valids.append(xPos)
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
                valids.append(xPos)
            else:
                assert False
            
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
        lastXRowNum = compressRowNumbers(getLastXRows(board, numRowsToSave))
        
        if cycleBonus == 0:
            key = (lastXRowNum, shapeIndex, dirIndex)
            if key in seenStates:
                val = seenStates[key]
                cycleLength = shapeNum - val[1]
                cycleHeight = len(board) - val[0]
                shapesRemaining = n - shapeNum
                cyclesToGo = shapesRemaining // cycleLength
                
                print("Cycle length:", cycleLength)
                print("Cycle height:", cycleHeight)
                print("Shapes remaining:", shapesRemaining)
                print("Cycles left to go: ", cyclesToGo)
                
                # Advance by cycles
                cycleBonus += cyclesToGo * cycleHeight
                i += cyclesToGo * cycleLength
                # Shape index is still correct
                # The board up to the last X rows should also look the same,
                # so we don't need to actually extend the length of the board
            else:
                seenStates[key] = (len(board), shapeNum)
        if shapeNum == stopAt:
            print(lastXRowNum)
            print(i, xPos, yPos)
            print("".join(dirs))
            print("".join([str(x) for x in valids]))
            for s in shape:
                print((" " * (xPos + 1)) + "".join(["@" if r == 1 else " " for r in s]))
            print()
            for row in board[::-1]:
                print("|" + "".join(["#" if r == 1 else "." for r in row]) + "|", rowToNumber(row))
            print("HEIGHT", len(board))
            
        # Increment
        i += 1
    print("FINAL", len(board) + cycleBonus)
    
if __name__ == "__main__":
    main()