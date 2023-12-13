import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def rot_90(l):
    return ["".join(list(reversed(x))) for x in zip(*l)]

def num_differences(a, b):
    num = 0
    for ch1, ch2 in zip(a, b):
        if ch1 != ch2:
            num += 1
    return num

def get_mirror_index(grid):
    candidates = []
    for index in range(len(grid) - 1):
        if num_differences(grid[index], grid[index + 1]) <= 1:
            candidates.append(index)
    
    for rowCandidate in candidates:
        firstHalf = rowCandidate
        secondHalf = rowCandidate + 1
        totalDiff = 0
        while firstHalf >= 0 and secondHalf < len(grid):
            totalDiff += num_differences(grid[firstHalf], grid[secondHalf])
            if totalDiff > 1:
                break
            firstHalf -= 1
            secondHalf += 1
        if totalDiff == 1:
            return rowCandidate + 1
    return -1

def process_grid(grid):
    rowMirrorIndex = get_mirror_index(grid)
    if rowMirrorIndex > -1:
        return (rowMirrorIndex, 0)
    
    colMirrorIndex = get_mirror_index(rot_90(grid))
    if colMirrorIndex > -1:
        return (0, colMirrorIndex)
    
    print("FAIL")
    return (0, 0)
    
        
    
def main():
    grids = []
    grid = []
    for line in lines:
        if not line:
            grids.append(grid)
            grid = []
            continue
        grid.append(line)
    grids.append(grid)
    
    result = (0, 0)
    for grid in grids:
        result = addT(result, process_grid(grid))
    numRows, numCols = result
    print(numCols + 100 * numRows)

if __name__ == "__main__":
    main()