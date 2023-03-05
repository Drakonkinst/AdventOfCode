import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

# Brute-forcing the solution
def main():
    target = int(lines[0])
    
    if target <= 1:
        print(0)
        return
    
    directions = [UP, LEFT, DOWN, RIGHT]
    
    x = 0
    y = 0
    currValue = 1
    ring = 0
    currDirectionIndex = 3
    distanceAlongEdge = 0
    spiral = {}
    spiral[(x, y)] = 1
    
    while currValue < target:
        ringWidth = 2 * ring + 1
        edgeDistance = ringWidth - 2
        spiral[(x, y)] = currValue
        hasMoved = False
        
        if distanceAlongEdge >= edgeDistance:
            currDirectionIndex += 1
            if currDirectionIndex >= len(directions):
                currDirectionIndex = 0
                ring += 1
                # Rings always extend to the right
                x, y = addT((x, y), RIGHT)
                hasMoved = True
                distanceAlongEdge = 0
            else:
                distanceAlongEdge = 0
        else:
            distanceAlongEdge += 1
        
        if not hasMoved:
            x, y = addT((x, y), directions[currDirectionIndex])
        currValue += 1
    manhattanDistance = abs(x) + abs(y)
    print(manhattanDistance)

if __name__ == "__main__":
    main()