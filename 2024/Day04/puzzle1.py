import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]
SEARCH_WORD = "XMAS"

def main():
    grid = [list(line) for line in lines]
    total = 0
    # 8 possible directions to search
    for _ in range(4):
        total += search_grid(grid)
        total += search_grid_diagonal(grid)
        grid = rot_90(grid)
    print(total)

def search_grid(grid):
    total = 0
    for row in grid:
        total += search_row(row)
    return total

def search_row(row):
    num_cols = len(row)
    col = 0
    total = 0
    current_step = 0
    while col < num_cols:
        ch = row[col]
        if ch == SEARCH_WORD[current_step]:
            current_step += 1
            if current_step >= len(SEARCH_WORD):
                total += 1
                current_step = 0
        else:
            if current_step > 0:
                current_step = 0
                col -= 1
        col += 1
    return total

def search_grid_diagonal(grid):
    grid_width = len(grid) # We can assume it is a square
    num_items_in_diagonal = 0
    total = 0
    for i in range(grid_width):
        num_items_in_diagonal += 1
        total += search_ascending_diagonal(grid, num_items_in_diagonal)

    for i in range(grid_width - 1):
        num_items_in_diagonal -= 1
        total += search_descending_diagonal(grid, num_items_in_diagonal)

    return total

def search_ascending_diagonal(grid, num_items_in_diagonal):
    diagonal = []
    for i in range(num_items_in_diagonal):
        row = num_items_in_diagonal - i - 1
        col = i
        diagonal.append(grid[row][col])
    return search_row(diagonal)

def search_descending_diagonal(grid, num_items_in_diagonal):
    grid_width = len(grid)
    diagonal = []
    for i in range(num_items_in_diagonal):
        row = (grid_width - 1) - i
        col = grid_width - num_items_in_diagonal + i
        diagonal.append(grid[row][col])
    return search_row(diagonal)

if __name__ == "__main__":
    main()