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
        instrs.append((CARDINAL_NEIGHBORS[DIRS.index(w[0])], int(w[1]), int(w[2][2:-1], 16)))
        
    edges = set()
    inside = set()
    edges.add((0, 0))
    x = 0
    y = 0
    for (direction, numCubes, colorInt) in instrs:
        for i in range(numCubes):
            x += direction[0]
            y += direction[1]
            
            if direction == UP:
                inside.add((x - 1, y))
            elif direction == DOWN:
                inside.add((x + 1, y))
            elif direction == RIGHT:
                inside.add((x, y - 1))
            elif direction == UP:
                inside.add((x, y + 1))
            edges.add((x, y))
    assert x == 0 and y == 0
    
    xVals = [edge[0] for edge in edges]
    yVals = [edge[1] for edge in edges]
    minX = min(xVals)
    maxX = max(xVals)
    minY = min(yVals)
    maxY = max(yVals)
    print(minX, maxX, minY, maxY)
    
    inside = inside.difference(edges)
    insidePos = next(iter(inside))
    q = deque()
    q.append(insidePos)
    v = set()
    v.add(insidePos)
    print("START", insidePos, len(edges))
    while q:
        pos = q.pop()
        (x, y) = pos
        if(len(q) > 100000):
            break
        if not (minX <= x <= maxX) or not (minY <= y <= maxY):
            print("WRONG START")
            return
        for (xOffset, yOffset) in CARDINAL_NEIGHBORS:
            nextPos = (x + xOffset, y + yOffset)
            if nextPos in v or nextPos in edges:
                continue
            v.add(nextPos)
            q.append(nextPos)
    v = v.difference(edges)
    print(len(edges) + len(v))
    
if __name__ == "__main__":
    main()