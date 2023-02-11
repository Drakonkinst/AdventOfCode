import sys
from collections import deque

def main():
    file = open("input.txt", "r")
    lines = [line for line in file.readlines()]
    
    y = 0
    walls = set()
    rowDims = []
    maxX = -1
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
        rowDims.append((lo, hi))
        y += 1

    height = y
    width = maxX + 1
    colDims = []
    for x in range(width):
        lo = sys.maxsize
        hi = -1
        for y in range(len(rowDims)):
            interval = rowDims[y]
            if interval[0] <= x <= interval[1]:
                lo = min(lo, y)
                hi = max(hi, y)
        colDims.append((lo, hi))
    
    x = rowDims[0][0] # x
    y = 0             # y
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
                offset = dirs[facingDir]
                #print("Received", toMove, offset)
                for i in range(toMove):
                    nextX = x + offset[0]
                    nextY = y + offset[1]
                    xChanged = x != nextX
                    
                    # Validate bounds
                    if xChanged:
                        if nextX < 0:
                            nextX = rowDims[nextY][1]
                        elif nextX >= width:
                            nextX = rowDims[nextY][0]
                        rowDim = rowDims[nextY]
                        validRow = rowDim[0] <= nextX <= rowDim[1]
                        if not validRow:
                            if nextX > rowDim[1]:
                                nextX = rowDim[0]
                            else:
                                nextX = rowDim[1]
                    else:
                        if nextY < 0:
                            nextY = colDims[nextX][1]
                        elif nextY >= height:
                            nextY = colDims[nextX][0]
                        colDim = colDims[nextX]
                        validCol = colDim[0] <= nextY <= colDim[1]
                        if not validCol:
                            if nextY > colDim[1]:
                                nextY = colDim[0]
                            else:
                                nextY = colDim[1]
                    
                    if (nextX, nextY) in walls:
                        break
                    x = nextX
                    y = nextY
                    #print("MOVE", (x, y))
                #print("DONE", (x, y))
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