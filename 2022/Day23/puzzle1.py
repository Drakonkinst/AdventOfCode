import sys
from collections import deque

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def findBounds(allElves):
    maxX = -sys.maxsize
    minX = sys.maxsize
    maxY = -sys.maxsize
    minY = sys.maxsize
    for x, y in allElves:
        maxX = max(x, maxX)
        minX = min(x, minX)
        maxY = max(y, maxY)
        minY = min(y, minY)
    return minX, maxX, minY, maxY

def display(name, allElves):
    return
    s = name + '\n'
    minX, maxX, minY, maxY = findBounds(allElves)
    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            if (x, y) in allElves:
                s += '#'
            else:
                s += '.'
        s += '\n'
    print(s)

def main():
    file = open("input.txt", "r")
    lines = [line.strip() for line in file.readlines()]
    
    allElves = set()
    y = 0
    for line in lines:
        x = 0
        for ch in line:
            if ch == '#':
                allElves.add((x, y))
            x += 1
        y += 1
    
    dirs = [
        [(0, -1), (1, -1), (-1, -1)],
        [(0, 1), (1, 1), (-1, 1)],
        [(-1, 0), (-1, -1), (-1, 1)],
        [(1, 0), (1, -1), (1, 1)]
    ]
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    dirToStart = 0
    n = 10
    display("INITIAL", allElves)
    for i in range(n):
        # Propose directions
        planned = {}
        numMoving = 0
        for elfPos in allElves:
            # Decide whether elf wants to move
            wantToMove = False
            for neighborOffset in neighbors:
                if add(elfPos, neighborOffset) in allElves:
                    wantToMove = True
                    break
            
            if not wantToMove:
                if elfPos not in planned:
                    planned[elfPos] = [elfPos]
                continue
            
            # Consider moving
            dirToConsider = dirToStart
            
            for j in range(len(dirs)):
                dirToMove = dirs[dirToConsider]
                cellToMove = add(elfPos, dirToMove[0])
                
                # If can move to this location
                # Check that all three locations do not currently have an elf
                if cellToMove not in allElves and add(elfPos, dirToMove[1]) not in allElves and add(elfPos, dirToMove[2]) not in allElves:
                    # Valid proposal
                    if cellToMove not in planned:
                        planned[cellToMove] = []
                    planned[cellToMove].append(elfPos)
                    numMoving += 1
                    wantToMove = False
                    break
                dirToConsider = (dirToConsider + 1) % len(dirs)
            if wantToMove:
                # No valid proposal, just stay still
                if elfPos not in planned:
                    planned[elfPos] = [elfPos]
        
        dirToStart = (dirToStart + 1) % len(dirs)
        
        # Check if no proposals, done
        if numMoving <= 0:
            break
        
        # Resolve movements
        newElfPositions = set()
        for k, v in planned.items():
            if len(v) <= 1:
                # Valid
                newElfPositions.add(k)
            else:
                # Invalid collision
                for item in v:
                    newElfPositions.add(item)
        assert len(allElves) == len(newElfPositions)
        allElves = newElfPositions
        display("ITERATION " + str(i + 1), allElves)

    display("FINAL", allElves)
    
    # Find bounds
    minX, maxX, minY, maxY = findBounds(allElves)
    totalArea = (maxX - minX + 1) * (maxY - minY + 1)
    numElves = len(allElves)
    
    print("ANS", totalArea - numElves)
if __name__ == "__main__":
    main()