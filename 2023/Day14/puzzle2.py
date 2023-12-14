import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def rollToLeft(grid):
    for row in grid:
        index = 0
        while index < len(row):
            ch = row[index]
            if ch == ".":
                nextFall = index
                while index < len(row):
                    if row[index] == "O":
                        row[index] = "."
                        row[nextFall] = "O"
                        index = nextFall
                        break
                    if row[index] == "#":
                        break
                    index += 1
            index += 1

def get_load(grid):
    total = 0
    for row in grid:
        for i in range(len(row)):
            if row[i] == "O":
                total += len(row) - i
    return total
    
def do_cycle(grid):
    rollToLeft(grid)
    grid = rot_90(grid)
    rollToLeft(grid)
    grid = rot_90(grid)
    rollToLeft(grid)
    grid = rot_90(grid)
    rollToLeft(grid)
    grid = rot_90(grid)
    load = get_load(grid)
    return (grid, load)

def main():
    grid = []
    for line in lines:
        grid.append(line)
    grid = rot_90(rot_90(rot_90(grid)))
    
    lastSeenIndices = {}
    sequence = []
    finalCycleStart = -1
    finalCycleLen = -1
    i = 0
    target = 1000000000
    currentLoad = 0
    while True:
        (grid, load) = do_cycle(grid)
        currentLoad = load
        sequence.append(load)
        if load in lastSeenIndices:
            lastSeen = lastSeenIndices[load]
            cycleLength = i - lastSeenIndices[load]
            if lastSeen >= cycleLength and cycleLength > 3:
                firstHalf = sequence[lastSeen+1:]
                secondHalf = sequence[lastSeen - cycleLength + 1:lastSeen+1]
                if all(num1 == num2 for num1, num2 in zip(firstHalf, secondHalf)):
                    finalCycleStart = lastSeen - cycleLength + 1
                    finalCycleLen = cycleLength
                    break
        lastSeenIndices[load] = i
        i += 1
        
        # if i == 3:
        #     rotated = rot_90(grid)
        #     print("\n".join(["".join(row) for row in rotated]), currentLoad)
    
    remaining = target - finalCycleStart
    #print(sequence, finalCycleLen, finalCycleStart, remaining, remaining % finalCycleLen)
    
    for j in range(remaining % finalCycleLen):
        (grid, load) = do_cycle(grid)
        currentLoad = load
    print(currentLoad)

if __name__ == "__main__":
    main()