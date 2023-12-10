import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

# This passes the test cases but not the actual puzzle, so I'm stumped. Gonna try a different approach

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
    
    # Find all discrete groups
    pathSet = set(cyclePath)
    visited = set()
    allGroups = []
    for row in range(numRows):
        for col in range(numCols):
            if (row, col) in visited:
                continue
            if (row, col) in pathSet:
                continue
            group = set()
            q = deque()
            q.append((row, col))
            while q:
                (r, c) = q.pop()
                visited.add((r, c))
                group.add((r, c))
                for (offsetCol, offsetRow) in CARDINAL_NEIGHBORS:
                    neighborRow = r + offsetRow
                    neighborCol = c + offsetCol
                    if (neighborRow, neighborCol) in pathSet or (neighborRow, neighborCol) in visited:
                        continue
                    if 0 <= neighborRow < numRows and 0 <= neighborCol < numCols:
                        q.append((neighborRow, neighborCol))
            allGroups.append(group)
    
    # Mark tiles inside/outside path by following it
    outsidePath = set()
    insidePath = set()
    print(cyclePath)
    for i in range(len(cyclePath) - 1):
        (row, col) = cyclePath[i]
        (nextRow, nextCol) = cyclePath[i + 1]
        direction = (nextRow - row, nextCol - col)
        if direction == UP:
            insidePath.add(addT((row, col), LEFT))
            outsidePath.add(addT((row, col), RIGHT))
        elif direction == LEFT:
            insidePath.add(addT((row, col), DOWN))
            outsidePath.add(addT((row, col), UP))
        elif direction == RIGHT:
            insidePath.add(addT((row, col), UP))
            outsidePath.add(addT((row, col), DOWN))
        else:
            # DOWN
            insidePath.add(addT((row, col), RIGHT))
            outsidePath.add(addT((row, col), LEFT))
    
    numInside = 0
    numNotInside = 0
    for group in allGroups:
        # Check if they were marked by the flood fill
        matchingInside = len(group.intersection(insidePath))
        matchingOutside = len(group.intersection(outsidePath))
        assert matchingInside == 0 or matchingOutside == 0 and not (matchingInside == 0 and matchingOutside == 0)
        if matchingOutside > 0:
            numNotInside += len(group)
            continue
        
        numInside += len(group)
    print(numInside, numNotInside)
    print(numInside)
        
if __name__ == "__main__":
    main()