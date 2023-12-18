import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

DIRS = "DRUL"

def main():
    instrs = []
    for line in lines:
        w = words(line)
        hexVal = w[2][2:-1]
        distance = int(hexVal[:-1], 16)
        dirDig = int(hexVal[-1], 16)
        if dirDig == 0:
            direction = RIGHT
        elif dirDig == 1:
            direction = UP
        elif dirDig == 2:
            direction = LEFT
        elif dirDig == 3:
            direction = DOWN
        else:
            print("PARSEFAIL")
            return
        instrs.append((direction, distance))
        
    x = 0
    y = 0
    yEdges = {}
    inside = {}
    minX = math.inf
    maxX = -math.inf
    minY = math.inf
    maxY = -math.inf

    
    # Get all edges
    i = 0
    for (direction, numCubes) in instrs:
        i += 1
        boxMinX = x
        boxMaxX = x
        boxMinY = y
        boxMaxY = y
        if direction == RIGHT:
            boxMaxX += numCubes
            x += numCubes
        elif direction == LEFT:
            boxMinX -= numCubes
            x -= numCubes
        elif direction == (0, 1):
            boxMaxY += numCubes
            y += numCubes
        elif direction == (0, -1):
            boxMinY -= numCubes
            y -= numCubes
        
        minX = min(x, minX)
        minY = min(y, minY)
        maxX = max(x, maxX)
        maxY = max(y, maxY)
        
        for boxY in range(boxMinY, boxMaxY + 1):
            if boxY not in yEdges:
                yEdges[boxY] = []
            yEdges[boxY].append((boxMinX, boxMaxX))
            
            if direction == (0, 1):
                if boxY not in inside:
                    inside[boxY] = set()
                inside[boxY].add(boxMaxX + 1)
            elif direction == (0, -1):
                if boxY not in inside:
                    inside[boxY] = set()
                inside[boxY].add(boxMinX - 1)
    assert x == 0 and y == 0
    
    # Clean up edges
    for y in yEdges:
        yEdge = yEdges[y]
        yEdge.sort()
        q = []
        # Compress intervals
        for lo, hi in yEdge:
            if len(q) <= 0:
                q.append([lo, hi])
                continue
            currMax = q[-1][1]
            if lo > currMax + 1:
                q.append([lo, hi])
                continue
            q[-1][1] = max(currMax, hi)
        yEdges[y] = q
    
    total = 0
    for y in yEdges:
        total_for_y = 0
        yEdge = yEdges[y]
        
        index = 0
        while index < len(yEdge) - 1:
            total_for_y += yEdge[index][1] - yEdge[index][0] + 1
            # If the next index is inside, add the interval in between
            if y in inside and (yEdge[index][1] + 1) in inside[y]:
                total_for_y += yEdge[index + 1][0] - yEdge[index][1] - 1
            index += 1
        total_for_y += yEdge[-1][1] - yEdge[-1][0] + 1
        total += total_for_y
    print(total)
        
if __name__ == "__main__":
    main()