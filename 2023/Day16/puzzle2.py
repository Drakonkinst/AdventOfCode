import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

grid = []
for line in lines:
    grid.append(line)
numRows = len(grid)
numCols = len(grid[0])

def get_energized(startRow, startCol, startDir):
    energized = set()
    processed = set()
    
    q = deque()
    q.append((startDir, startCol, startRow))
    while q:
        item = q.pop()
        if item in processed:
            continue
        processed.add(item)
        (direction, col, row) = item
        if (0 <= row < numRows) and (0 <= col < numCols):
            energized.add((row, col))
        nextCol = col + direction[0]
        nextRow = row + direction[1]
        if not (0 <= nextRow < numRows) or not (0 <= nextCol < numCols):
            continue
        ch = grid[nextRow][nextCol]
        if ch == ".":
            q.append((direction, nextCol, nextRow))
        if ch == "|":
            if direction[0] != 0:
                q.append((UP, nextCol, nextRow))
                q.append((DOWN, nextCol, nextRow))
            else:
                q.append((direction, nextCol, nextRow))
        if ch == "-":
            if direction[1] != 0:
                q.append((LEFT, nextCol, nextRow))
                q.append((RIGHT, nextCol, nextRow))
            else:
                q.append((direction, nextCol, nextRow))
        if ch == "/":
            if direction == RIGHT:
                nextDirection = UP
            elif direction == LEFT:
                nextDirection = DOWN
            elif direction == UP:
                nextDirection = RIGHT
            elif direction == DOWN:
                nextDirection = LEFT
            q.append((nextDirection, nextCol, nextRow))
        if ch == "\\":
            if direction == RIGHT:
                nextDirection = DOWN
            elif direction == LEFT:
                nextDirection = UP
            elif direction == UP:
                nextDirection = LEFT
            elif direction == DOWN:
                nextDirection = RIGHT
            q.append((nextDirection, nextCol, nextRow))
    return len(energized)

def main():
    maxVal = 0
    for i in range(numCols):
        top = get_energized(-1, i, DOWN)
        maxVal = max(maxVal, top)
        bot = get_energized(numRows, i, UP)
        maxVal = max(maxVal, bot)
    for i in range(numRows):
        left = get_energized(i, -1, RIGHT)
        maxVal = max(maxVal, left)
        right = get_energized(i, numCols, LEFT)
        maxVal = max(maxVal, right)
    print(maxVal)

if __name__ == "__main__":
    main()