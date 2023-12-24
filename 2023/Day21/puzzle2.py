import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

# Using approach from Reddit to deriving a polynomial from 3 specific points

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]
grid = lines


def find_in_grid(grid, ch):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == ch:
                return (row, col)
    assert False

def get(row, col):
    # Works for negatives too, thankfully
    (row, col) = modulo(row, col)
    return grid[row][col]
    
def modulo(row, col):
    return (row % len(grid), col % len(grid[0]))

def get_steps_for_max(maxSteps, startRow, startCol):
    q = deque()
    q.append((0, startRow, startCol))
    visited = set()
    canReach = set()
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
    return len(canReach)

def main():
    grid = lines
    # It's a square
    assert len(grid) == len(grid[0])
    size = len(grid)
    offset = size // 2
    
    startRow, startCol = find_in_grid(grid, "S")
    # These values work because for the puzzle, target % size = size // 2
    x = [offset, size + offset, size * 2 + offset]
    y = [get_steps_for_max(maxSteps, startRow, startCol) for maxSteps in x]
    # print(x)
    # print(y)
    
    # Determine polynomials from 3 points
    # Padded with 0 to match the formula
    # y1 = a * x1^2 + b * x1 + c
    # y2 = a * x2^2 + b * x2 + c
    # y3 = a * x3^3 + b * x3 + c
    
    # https://math.stackexchange.com/questions/680646/get-polynomial-function-from-3-points
    # Can simplify by scaling down the differences between x values, and scaling the target value accordingly
    a = (y[2] - (2 * y[1]) + y[0]) // 2
    b = y[1] - y[0] - a
    c = y[0]
    
    n = (26501365 - offset) // size
    result = (a * n**2) + (b * n) + c
    print(result)
        
if __name__ == "__main__":
    main()