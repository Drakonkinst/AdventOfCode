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

def main():
    file = open("input.txt", "r")
    directions = file.readlines()[0].strip()
    
    board = []
    n = 2022
    dirIndex = 0
    
    stopAt = n + 1
    
    i = 0
    while i < n:
        xPos = 2
        yPos = len(board) + 3
        shape = shapes[i % len(shapes)]
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
        if i + 1 == stopAt:
            print(i, xPos, yPos)
            print("".join(dirs))
            print("".join([str(x) for x in valids]))
            for s in shape:
                print((" " * (xPos + 1)) + "".join(["@" if r == 1 else " " for r in s]))
            print()
            for row in board[::-1]:
                print("|" + "".join(["#" if r == 1 else "." for r in row]) + "|")
            print("HEIGHT", len(board))
            
        # Increment
        i += 1
    print("FINAL", len(board))
    
if __name__ == "__main__":
    main()