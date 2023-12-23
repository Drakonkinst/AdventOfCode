import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]
grid = lines
canReach = set()

def find_in_grid(grid, ch):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == ch:
                return (row, col)
    assert False

def print_grid(grid, get_char_for_pos):
    for row in range(len(grid)):
        s = ""
        for col in range(len(grid[0])):
            s += get_char_for_pos(row, col)
        print(s)

def get_char(row, col):
    if (row, col) in canReach:
        return "O"
    return grid[row][col]

def main():
    grid = lines
    
    numRows = len(grid)
    numCols = len(grid[0])
    startRow, startCol = find_in_grid(grid, "S")
    
    q = deque()
    q.append((0, startRow, startCol))
    visited = set()
    
    maxSteps = 10
    while q:
        (step, row, col) = q.popleft()
        key = (step % 2 == 0, row, col)
        if key in visited:
            continue
        visited.add(key)
        
        if step % 2 == 0:
            canReach.add((row, col))
        
        if step >= maxSteps:
            continue
        
        for (offsetCol, offsetRow) in CARDINAL_NEIGHBORS:
            nextRow = row + offsetRow
            nextCol = col + offsetCol
            if not (0 <= nextRow < numRows and 0 <= nextCol < numCols):
                continue
            if grid[nextRow][nextCol] != ".":
                continue
            
            q.append((step + 1, nextRow, nextCol))
    
    print_grid(grid, get_char)
    print(len(canReach))
    
if __name__ == "__main__":
    main()