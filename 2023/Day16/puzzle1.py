import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    grid = []
    for line in lines:
        grid.append(line)
    numRows = len(grid)
    numCols = len(grid[0])

    energized = set()
    processed = set()
    
    q = deque()
    q.append((RIGHT, -1, 0))
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
    print(len(energized))
    
    s = ""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (row, col) in energized:
                s += "#"
            else:
                s += grid[row][col]
        s += "\n"
    print(s)
            

if __name__ == "__main__":
    main()