import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    grid = make_grid((1000, 1000), 0)
    for line in lines:
        x1, y1, x2, y2 = ints(line)
        op = -1
        if line.startswith("turn off"):
            op = 0
        elif line.startswith("turn on"):
            op = 1
        elif line.startswith("toggle"):
            op = 2
        else:
            assert False
        
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if op == 0:
                    grid[x][y] = max(0, grid[x][y] - 1)
                if op == 1:
                    grid[x][y] += 1
                if op == 2:
                    grid[x][y] += 2
    print(sum(map(sum, grid)))

if __name__ == "__main__":
    main()