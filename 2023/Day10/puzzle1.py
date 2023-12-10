import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

# north, east, south, west
charToPipe = {
    "|": (True, False, True, False),
    "-": (False, True, False, True),
    "L": (True, True, False, False),
    "J": (True, False, False, True),
    "7": (False, False, True, True),
    "F": (False, True, True, False),
    ".": (False, False, False, False)
}

def main():
    # Parse grid
    grid = []
    for line in lines:
        grid.append([ch for ch in line])
    
    # Find cycle
    numRows = len(grid)
    numCols = len(grid[0])
    startRow = 0
    startCol = 0
    found = False
    while startRow < numRows:
        startCol = 0
        while startCol < numCols:
            ch = grid[startRow][startCol]
            if ch == "S":
                found = True
                break
            startCol += 1
        if found:
            break
        startRow += 1
        
    #print("START", (startRow, startCol))
    
    candidates = []
    for i in range(len(CARDINAL_NEIGHBORS)):
        # Get pipe
        (offsetCol, offsetRow) = CARDINAL_NEIGHBORS[i]
        row = startRow + offsetRow
        col = startCol + offsetCol
        charAtOffset = grid[row][col]
        pipe = charToPipe[charAtOffset]
        
        # Check if pipe is directed at S
        oppositeDirIndex = (i + 2) % 4
        isFacingStart = pipe[oppositeDirIndex]
        if isFacingStart:
            candidates.append((row, col))
    
    #print("CANDIDATES", candidates)
    
    cyclePath = None
    for (candidateRow, candidateCol) in candidates:
        path = [(startRow, startCol), (candidateRow, candidateCol)]
        row = candidateRow
        col = candidateCol
        
        while True:
            ch = grid[row][col]
            pipe = charToPipe[ch]
            nextRow = None
            nextCol = None
            numVisited = 0
            for i in range(len(pipe)):
                if not pipe[i]:
                    continue
                (offsetCol, offsetRow) = CARDINAL_NEIGHBORS[i]
                nextPos = (row + offsetRow, col + offsetCol)
                if nextPos in path:
                    numVisited += 1
                    if numVisited >= 2:
                        cyclePath = path
                        break
                    else:
                        continue
                # Unvisited path found
                path.append(nextPos)
                nextRow = nextPos[0]
                nextCol = nextPos[1]
            if nextRow is None:
                break
            row = nextRow
            col = nextCol
        if cyclePath is not None:
            break
    
    #print("CYCLE", cyclePath)
    print(len(cyclePath) // 2)
                
        
if __name__ == "__main__":
    main()