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
    ring = 0
    currDirectionIndex = 3
    distanceAlongEdge = 0
    spiral = {}
    spiral[(x, y)] = 1
    
    while True:
        ringWidth = 2 * ring + 1
        edgeDistance = ringWidth - 2
        hasMoved = False
        
        if x == 0 and y == 0:
            value = 1
            spiral[(x, y)] = 1
        else:
            value = 0
            for offsetX, offsetY in DIAGONAL_NEIGHBORS:
                pos = (x + offsetX, y + offsetY)
                if pos in spiral:
                    value += spiral[pos]
        
        if value > target:
            print(value)
            return
        else:
            spiral[(x, y)] = value
        
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
    print("FAIL")

if __name__ == "__main__":
    main()