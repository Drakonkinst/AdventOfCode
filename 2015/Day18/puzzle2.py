import sys, os, re, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    grid = make_grid((100, 100), False)
    y = 0
    for line in lines:
        for x in range(len(line)):
            grid[y][x] = line[x] == "#"
        y += 1
    grid[0][99] = True
    grid[99][0] = True
    grid[0][0] = True
    grid[99][99] = True
        
    n = 100
    for i in range(n):
        nextGrid = make_grid((100, 100), False)
        for y in range(100):
            for x in range(100):
                if (x == 0 or x == 100 - 1) and (y == 0 or y == 100 -1):
                    nextGrid[y][x] = True
                    continue
                v = grid[y][x]
                c = 0
                for dx, dy in DIAGONAL_NEIGHBORS:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < 100 and 0 <= ny < 100 and grid[ny][nx]:
                        c += 1
                if v:
                    nextGrid[y][x] = c == 2 or c == 3
                else:
                    nextGrid[y][x] = c == 3
        grid = nextGrid
    t = 0
    for y in range(100):
        for x in range(100):
            if grid[y][x]:
                t += 1
    print(t)

if __name__ == "__main__":
    main()