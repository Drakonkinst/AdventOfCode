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
    
    baseId = 0
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
                        dependencies[baseId].add(placed[key])
                        done = True
            if done:
                break
            if minZ - distanceFallen <= 1:
                break
            distanceFallen += 1
        bounds[2] = (bounds[2][0] - distanceFallen, bounds[2][1] - distanceFallen)
        maxPlacedZ = max(max(bounds[2]), maxPlacedZ)
        place_block(bounds, baseId, placed)
        baseId += 1
    
    # Invert dependency map
    inverted = [set() for _ in range(len(blocksToFall))]
    for baseId in range(len(dependencies)):
        for blockId in dependencies[baseId]:
            inverted[blockId].add(baseId)
    #print(dependencies)
    #print(inverted)
    
    total = 0
    for baseId in range(len(inverted)):
        q = deque()
        disintegrated = set()
        q.append(baseId)
        while q:
            blockId = q.popleft()
            for supportedId in inverted[blockId]:
                noOtherDependencies = True
                for dep in dependencies[supportedId]:
                    if dep in disintegrated or dep == blockId:
                        continue
                    noOtherDependencies = False
                    break
                
                if noOtherDependencies:
                    disintegrated.add(supportedId)
                    q.append(supportedId)
        total += len(disintegrated)
        # print(to_char(baseId), len(disintegrated))
    print(total)

if __name__ == "__main__":
    main()