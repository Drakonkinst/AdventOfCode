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
    regions = []
    visited = set()
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            pos = (row, col)
            if pos in visited:
                continue
            calculate_region(lines, pos, regions, visited)
    total = 0
    for region in regions:
        region_id, plot = region
        area = len(plot)
        perimeter = calculate_perimeter(plot)
        total += area * perimeter
    print(total)

def calculate_region(grid, start_pos, regions, visited):
    region_id = grid[start_pos[0]][start_pos[1]]
    q = deque()
    q.append(start_pos)
    plots = []
    while len(q):
        pos = q.pop()
        if pos in visited:
            continue
        visited.add(pos)
        plots.append(pos)
        for offset in CARDINAL_NEIGHBORS:
            neighbor_pos = addT(pos, offset)
            if not in_bounds(neighbor_pos, len(grid), len(grid[0])):
                continue
            neighbor_region_id = grid[neighbor_pos[0]][neighbor_pos[1]]
            if neighbor_region_id == region_id:
                q.append(neighbor_pos)
    regions.append((region_id, plots))

def calculate_perimeter(region):
    perimeter = 0
    for plot in region:
        for offset in CARDINAL_NEIGHBORS:
            next_plot = addT(plot, offset)
            if next_plot not in region:
                perimeter += 1
    return perimeter

if __name__ == "__main__":
    main()