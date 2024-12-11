import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]
pairs = [[(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]

def main():
    grid = [list(line) for line in lines]
    total = 0
    # Ignore outer edge, as no centers can be found there
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if check_for_xmas(grid, row, col):
                total += 1
    print(total)

def check_for_xmas(grid, row, col):
    if grid[row][col] != 'A':
        return False
    for pair in pairs:
        offset1, offset2 = pair
        # We can assume these are valid positions on the grid
        pos1 = addT((row, col), offset1)
        pos2 = addT((row, col), offset2)
        item1 = grid[pos1[0]][pos1[1]]
        item2 = grid[pos2[0]][pos2[1]]
        valid = (item1 == 'M' and item2 == 'S') or (item1 == 'S' and item2 == 'M')
        if not valid:
            return False
    return True

if __name__ == "__main__":
    main()