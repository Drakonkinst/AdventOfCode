import sys, os, itertools as itt
from collections import deque # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

sys.setrecursionlimit(10000)

# I forgot about the goal of getting to the bottom row, and it still worked
file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

walls = set()
arrows = [set() for _ in range(len(CARDINAL_NEIGHBORS))]
startPos = None
sizeY = len(lines)
sizeX = len(lines[0])

def get_longest_path(pos, visited, pathLength):
    foundArrowDir = None
    for index in range(len(arrows)):
        if pos in arrows[index]:
            foundArrowDir = CARDINAL_NEIGHBORS[index]
            break
    
    candidates = []
    for direction in CARDINAL_NEIGHBORS:
        if foundArrowDir is not None and foundArrowDir != direction:
            continue
        nextPos = addT(pos, direction)
        if nextPos in walls or nextPos in visited or not in_bounds(nextPos, sizeY, sizeX):
            continue
        candidates.append(nextPos)
    
    visited.add(pos)
    if len(candidates) <= 0:
        return pathLength
    elif len(candidates) == 1:
        return get_longest_path(candidates[0], visited, pathLength + 1)
    else:
        return max([get_longest_path(candidate, visited.copy(), pathLength + 1) for candidate in candidates])

def main():
    y = 0
    for line in lines:
        x = 0
        for ch in line:
            if ch == "#":
                walls.add((x, y))
            elif ch == ".":
                if y == 0:
                    startPos = (x, y)
            else:
                direction = arrow(ch)
                index = CARDINAL_NEIGHBORS.index(direction)
                arrows[index].add((x, y))
            x += 1
        y += 1
    
    print(get_longest_path(startPos, set([startPos]), 0))

if __name__ == "__main__":
    main()