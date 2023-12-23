import sys, os, itertools as itt
from collections import deque
from queue import PriorityQueue
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]
grid = [[int(ch) for ch in line] for line in lines]
numRows = len(grid)
numCols = len(grid[0])

def valid(row, col):
    return 0 <= row < numRows and 0 <= col < numCols

def main():
    start = (0, 0)
    end = (numRows - 1, numCols - 1)
    
    q = PriorityQueue()
    q.put((0, start, (0, 0)))
    
    v = set()
    while q:
        (heat, pos, direction) = q.get()
        if pos == end:
            print(heat)
            return
        key = (pos, direction)
        if key in v:
            continue
        v.add(key)
        (row, col) = pos
        for nextDirection in CARDINAL_NEIGHBORS:
            if direction[0] != 0 and nextDirection[0] != 0:
                continue
            if direction[1] != 0 and nextDirection[1] != 0:
                continue
            (offsetRow, offsetCol) = nextDirection
            nextHeat = heat
            for i in range(3):
                nextRow = row + offsetRow * (i + 1)
                nextCol = col + offsetCol * (i + 1)
                if not valid(nextRow, nextCol):
                    break
                nextHeat += grid[nextRow][nextCol]
                q.put((nextHeat, (nextRow, nextCol), nextDirection))

if __name__ == "__main__":
    main()