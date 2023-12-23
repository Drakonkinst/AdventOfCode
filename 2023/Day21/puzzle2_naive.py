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

def get(row, col):
    # Works for negatives too, thankfully
    (row, col) = modulo(row, col)
    return grid[row][col]
    
def modulo(row, col):
    return (row % len(grid), col % len(grid[0]))

def in_bounds(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def main():
    grid = lines
    startRow, startCol = find_in_grid(grid, "S")
    
    q = deque()
    q.append((0, startRow, startCol))
    visited = set()
    
    maxSteps = 10
    while q:
        (step, row, col) = q.popleft()
        key = (row, col)
        if key in visited:
            continue
        visited.add(key)
        
        if step % 2 == maxSteps % 2:
            canReach.add((row, col))
        
        if step >= maxSteps:
            continue
        
        for (offsetCol, offsetRow) in CARDINAL_NEIGHBORS:
            nextRow = row + offsetRow
            nextCol = col + offsetCol
            if get(nextRow, nextCol) == "#":
                continue
            q.append((step + 1, nextRow, nextCol))
    
    print(len(canReach))
    l = list(canReach)
    l.sort()
    print(l)
    #print_grid(grid, get_char)
    
if __name__ == "__main__":
    main()