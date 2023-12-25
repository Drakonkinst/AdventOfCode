import sys, os, itertools as itt
from collections import deque # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def place_block(bounds, blockId, placed):
    for x in range(min(bounds[0]), max(bounds[0]) + 1):
        for y in range(min(bounds[1]), max(bounds[1]) + 1):
            for z in range(min(bounds[2]), max(bounds[2]) + 1):
                key = (x, y, z)
                assert key not in placed
                placed[key] = blockId

def to_char(num):
    return chr(num + ord("A"))

def graph(placed, axis1, axis2):
    axis1Vals = [x[axis1] for x in placed.keys()]
    axis2Vals = [x[axis2] for x in placed.keys()]
    min1 = min(axis1Vals)
    max1 = max(axis1Vals)
    min2 = min(axis2Vals)
    max2 = max(axis2Vals)
    
    grid = []
    for a2 in range(max2, min2 - 1, -1):
        line = []
        for a1 in range(min1, max1 + 1):
            line.append(".")
        grid.append(line)
    
    for coords in placed:
        val1 = coords[axis1]
        val2 = coords[axis2]
        grid[max2 - val2][val1 - min1] = to_char(placed[coords])
    
    for row in grid:
        print("".join(row))
            
    
def main():
    blocksToFall = []
    for line in lines:
        coords = line.split("~")
        blockStart = ints(coords[0])
        blockEnd = ints(coords[1])
        blocksToFall.append((blockStart, blockEnd))
    blocksToFall.sort(key=lambda x:min(x[0][2], x[1][2]))
    
    blockId = 0
    dependencies = [set() for _ in range(len(blocksToFall))]
    placed = {}
    maxPlacedZ = 0
    for block in blocksToFall:
        (start, end) = block
        bounds = list(zip(start, end))
        minZ = min(bounds[2])
        distanceFallen = 0
        done = False
        while not done:
            # Check along the bottom of the block for collisions
            for x in range(min(bounds[0]), max(bounds[0]) + 1):
                for y in range(min(bounds[1]), max(bounds[1]) + 1):
                    key = (x, y, minZ - distanceFallen - 1)
                    if key in placed:
                        dependencies[blockId].add(placed[key])
                        done = True
            if done:
                break
            if minZ - distanceFallen <= 1:
                break
            distanceFallen += 1
        bounds[2] = (bounds[2][0] - distanceFallen, bounds[2][1] - distanceFallen)
        maxPlacedZ = max(max(bounds[2]), maxPlacedZ)
        place_block(bounds, blockId, placed)
        blockId += 1
    
    canBeRemoved = set([blockId for blockId in range(len(dependencies))])
    for baseId in range(len(dependencies)):
        if len(dependencies[baseId]) == 1:
            for supportingId in dependencies[baseId]:
                if supportingId in canBeRemoved:
                    canBeRemoved.remove(supportingId)
    
    # graph(placed, 0, 2)
    # print()
    # graph(placed, 1, 2)
    # print()
    
    #print([to_char(i) for i in canBeRemoved])
    print(len(canBeRemoved))
    

if __name__ == "__main__":
    main()