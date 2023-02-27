import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *
from copy import deepcopy

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

nodes = {}
neverMove = set()
width = 31
height = 34

# width = 3
# height = 3

nodeSizes = make_grid((height, width), None)

def make_state(grid, minVal, maxVal):
    flat = []
    for x in range(height):
        for y in range(width):
            size = nodeSizes[x][y]
            used = grid[x][y]
            avail = size - used
            if avail < minVal:
                flat.append(False)
            elif avail >= maxVal:
                flat.append(True)
            else:
                flat.append(used)
    return tuple(flat)

def viable(coordsA, coordsB, nodeUsed):
    if coordsA == coordsB:
        return False
    aX, aY = coordsA
    bX, bY = coordsB
    usedA = nodeUsed[aX][aY]
    usedB = nodeUsed[bX][bY]
    sizeB = nodeSizes[bX][bY]
    availB = sizeB - usedB
    return usedA > 0 and usedA <= availB

def transfer(coordsA, coordsB, nodeUsed):
    aX, aY = coordsA
    bX, bY = coordsB
    usedA = nodeUsed[aX][aY]
    nodeUsed[aX][aY] = 0
    nodeUsed[bX][bY] += usedA
    
def is_valid(node):
    x, y = node
    return 0 <= x < height and 0 <= y < width and nodeSizes[x][y] is not None

def print_grid(grid):
    for row in grid:
        s = ""
        for x in row:
            s += str(x).zfill(3) + " "
        print(s)

def main():
    l = lines[2:]
    nodeUsed = make_grid((height, width), None)
    goal = (height - 1, 0)
    nodeList = []
    for line in l:
        nums = tuple(ints(line))
        x, y, size, used, avail, usePerc = nums
        nodeSizes[x][y] = size
        nodeUsed[x][y] = used
        nodeList.append((x, y))
    
    minUsed = 999
    maxUsed = 0
    for x in range(height):
        for y in range(width):
            # Can it move to another node in any situation?
            used = nodeUsed[x][y]
            if used < 100:
                minUsed = min(minUsed, used)
                maxUsed = max(maxUsed, used)
            else:
                currNode = (x, y)
                neverMove.add(currNode)
    print(minUsed, maxUsed)
    #print_grid(nodeUsed)
    
    q = deque([(0, goal, nodeUsed)])
    v = set()
    lastStep = -1
    while len(q) > 0:
        step, goalPos, nodes = q.popleft()
        
        state = (goalPos, make_state(nodes, minUsed, maxUsed))
        if state in v:
            continue
        v.add(state)
        
        if goalPos == (0, 0):
            print("ANS", step)
            return
        
        if step > lastStep:
            lastStep = step
            print("STEP", step, len(q))
        
        for x in range(height):
            for y in range(width):
                currNode = (x, y)
                if nodes[x][y] == 0 or currNode in neverMove:
                    continue
                for xOffset, yOffset in CARDINAL_NEIGHBORS:
                    nextNode = (x + xOffset, y + yOffset)
                    if currNode == goalPos and nextNode in neverMove:
                        continue
                    if is_valid(nextNode) and viable(currNode, nextNode, nodes):
                        # Never move the goal data to a node that it cannot move out of
                        nodesCopy = deepcopy(nodes)
                        transfer(currNode, nextNode, nodesCopy)
                        #print_grid(nodesCopy)
                        
                        if currNode == goalPos:
                            #print(step, "MOVE GOAL", a, "->", b)
                            q.append((step + 1, nextNode, nodesCopy))
                        else:
                            #print(step, "MOVE NORMAL", a, "->", b)
                            q.append((step + 1, goalPos, nodesCopy))
                
    print("FAIL")

if __name__ == "__main__":
    main()