import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    # Read grid
    grid = []
    trailheads = []
    for row in range(len(lines)):
        line = lines[row]
        grid_row = []
        for col in range(len(line)):
            ch = line[col]
            if ch in DIGITS:
                value = int(ch)
            else:
                value = 999
            if value == 0:
                trailheads.append((row, col))
            grid_row.append(value)
        grid.append(grid_row)

    total = 0
    for trailhead in trailheads:
        total += get_trailhead_score(trailhead, grid)
    print(total)

def get_trailhead_score(trailhead, grid):
    q = deque()
    q.append((trailhead, 0))
    score = 0
    while len(q):
        pos, height = q.pop()
        if height == 9:
            score += 1
            continue
        for offset in CARDINAL_NEIGHBORS:
            neighbor_pos = addT(pos, offset)
            if in_bounds(neighbor_pos, len(grid), len(grid[0])):
                neighbor_value = grid[neighbor_pos[0]][neighbor_pos[1]]
                if neighbor_value == height + 1:
                    q.append((neighbor_pos, neighbor_value))
    return score

if __name__ == "__main__":
    main()