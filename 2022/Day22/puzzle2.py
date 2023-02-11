import sys
import math
from collections import deque


RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

def translateRelative(relativeX, relativeY, currentEdge, incomingDir, sideLength):
    if currentEdge == UP:
        #print("EXIT FROM UP")
        assert relativeY == 0
        if incomingDir == RIGHT:
            return (sideLength - 1, sideLength - 1 - relativeX)
        elif incomingDir == DOWN:
            return (relativeX, sideLength - 1)
        elif incomingDir == LEFT:
            return (0, relativeX)
        elif incomingDir == UP:
            return (sideLength - 1 - relativeX, 0)
    elif currentEdge == DOWN:
        #print("EXIT FROM DOWN")
        assert relativeY == sideLength - 1
        if incomingDir == RIGHT:
            return (sideLength - 1, relativeX)
        elif incomingDir == DOWN:
            return (sideLength - 1 - relativeX, sideLength - 1)
        elif incomingDir == LEFT:
            return (0, sideLength - 1 - relativeX)
        elif incomingDir == UP:
            return (relativeX, 0)
    elif currentEdge == RIGHT:
        #print("EXIT FROM RIGHT")
        assert relativeX == sideLength - 1
        if incomingDir == RIGHT:
            return (sideLength - 1, sideLength - 1 - relativeY)
        elif incomingDir == DOWN:
            return (relativeY, sideLength - 1)
        elif incomingDir == LEFT:
            return (0, relativeY)
        elif incomingDir == UP:
            return (sideLength - 1 - relativeY, 0)
    elif currentEdge == LEFT:
        #print("EXIT FROM LEFT")
        assert relativeX == 0
        if incomingDir == RIGHT:
            return (sideLength - 1, relativeY)
        elif incomingDir == DOWN:
            return (sideLength - 1 - relativeY, sideLength - 1)
        elif incomingDir == LEFT:
            return (0, sideLength - 1 - relativeY)
        elif incomingDir == UP:
            return (relativeY, 0)
    assert False

def main():
    file = open("input.txt", "r")
    lines = [line for line in file.readlines()]
    
    walls = set()
    rowDims = []
    colDims = []
    y = 0
    maxX = -1
    lastRowDim = (-1, -1)
    
    # Populate rows
    for line in lines:
        line = line[:-1]
        if len(line) <= 0:
            break
        lo = sys.maxsize
        hi = -1
        for x in range(len(line)):
            ch = line[x]
            if ch == ' ':
                continue
            lo = min(x, lo)
            hi = max(x, hi)
            maxX = max(x, maxX)
            if ch == '#':
                walls.add((x, y))
        
        rowDim = (lo, hi)
        rowDims.append(rowDim)
        if lastRowDim != rowDim:
            lastRowDim = rowDim
        y += 1

    # Populate columns
    height = y
    width = maxX + 1
    lastColDim = (-1, -1)
    for x in range(width):
        lo = sys.maxsize
        hi = -1
        for y in range(len(rowDims)):
            interval = rowDims[y]
            if interval[0] <= x <= interval[1]:
                lo = min(lo, y)
                hi = max(hi, y)
        colDim = (lo, hi)
        colDims.append(colDim)
        if lastColDim != colDim:
            lastColDim = colDim

    sideLength = math.gcd(width, height)
    sidesMatrix = []
    topLeft = {}
    adjacent = {}
    
    # Label sides
    numSides = 0
    for row in range(0, height, sideLength):
        sidesRow = []
        for col in range(0, width, sideLength):
            colDim = colDims[col]
            rowDim = rowDims[row]
            validRow = rowDim[0] <= col <= rowDim[1]
            validCol = colDim[0] <= row <= colDim[1]
            if validRow and validCol:
                numSides += 1
                sidesRow.append(numSides)
                topLeft[numSides] = (col, row)
            else:
                sidesRow.append(0)
        sidesMatrix.append(sidesRow)

    for row in sidesMatrix:
        print(row)
        
    # Calculate adjacency - hardcoding this for now
    # right, down, left, up
    EXAMPLE = len(lines) == 14
    if EXAMPLE:
        adjacent = {
            1: [6, 4, 3, 2],
            2: [3, 5, 6, 1],
            3: [4, 5, 2, 1],
            4: [6, 5, 3, 1],
            5: [6, 2, 3, 4],
            6: [1, 2, 5, 4]
        }
    else:
        adjacent = {
            1: [2, 3, 4, 6],
            2: [5, 3, 1, 6],
            3: [2, 5, 4, 1],
            4: [5, 6, 1, 3],
            5: [2, 6, 4, 3],
            6: [5, 2, 1, 4]
        }
            
    # Start travel
    x = rowDims[0][0]
    y = 0
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    facingDir = 0
    digitStr = ""
    instr = lines[-1].strip() + "RRRR"
    
    for ch in instr:
        if ch.isdigit():
            digitStr += ch
        else:
            if len(digitStr) > 0:
                toMove = int(digitStr)
                digitStr = ""
                #print("Received", toMove)
                for i in range(toMove):
                    # Calculate side, assumes x and y are valid
                    sideX = x // sideLength
                    sideY = y // sideLength
                    sideMinX = sideX * sideLength
                    sideMaxX = sideMinX + sideLength - 1
                    sideMinY = sideY * sideLength
                    sideMaxY = sideMinY + sideLength - 1
                    sideNum = sidesMatrix[sideY][sideX]
                    
                    # Calculate offset based on facingDir
                    offset = dirs[facingDir]

                    # Set values if same side
                    nextX = x + offset[0]
                    nextY = y + offset[1]
                    nextDir = facingDir # Doesn't change unless not same side
                    
                    # Calculate if same side
                    sameSide = sideMinX <= nextX <= sideMaxX and sideMinY <= nextY <= sideMaxY
                    
                    # If no longer in the same side:
                    if not sameSide:
                        nextFace = adjacent[sideNum][facingDir]
                        incomingDir = adjacent[nextFace].index(sideNum)
                        topLeftX, topLeftY = topLeft[nextFace]
                        relativeX = x - sideMinX
                        relativeY = y - sideMinY
                        #print("RELATIVE", relativeX, relativeY)
                        #print("NEXT FACE:", nextFace)
                        
                        # Calculate new position and direction
                        xOffset, yOffset = translateRelative(relativeX, relativeY, facingDir, incomingDir, sideLength)
                        nextX = topLeftX + xOffset
                        nextY = topLeftY + yOffset
                        nextDir = (incomingDir + 2) % len(dirs)
                    
                    if (nextX, nextY) in walls:
                        #print("WALL", (nextX, nextY))
                        break
                    
                    x = nextX
                    y = nextY
                    facingDir = nextDir
                    #print("MOVE", (x, y))
            if ch == 'R':
                facingDir = (facingDir + 1) % len(dirs)
            elif ch == 'L':
                facingDir = (facingDir - 1 + len(dirs)) % len(dirs)
            else:
                assert False

    row = y + 1
    col = x + 1
    print(row, col, facingDir)
    print("ANS", 1000 * row + 4 * col + facingDir)
if __name__ == "__main__":
    main()