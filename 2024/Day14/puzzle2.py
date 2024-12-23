import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

TIME_ELAPSED = 100
WIDTH = 101
HEIGHT = 103

def main():
    bots = []
    for line in lines:
        start_x, start_y, velocity_x, velocity_y = ints(line)
        bots.append((start_x, start_y, velocity_x, velocity_y))

    # Look for contiguous bots in a row which form some base of the tree
    time = 0
    while True:
        positions = get_positions(bots, time)
        grid = create_grid(positions)
        contiguous = search_contiguous_positions(grid)
        if (contiguous):
            print_grid(grid)
            print(time)
            return
        time += 1

min_contiguous_streak = 10
def search_contiguous_positions(grid):
    for row in grid:
        contiguous_streak = 0
        for ch in row:
            if ch == '#':
                contiguous_streak += 1
            else:
                contiguous_streak = 0
            if contiguous_streak >= min_contiguous_streak:
                return True
    return False

def get_positions(bots, time_elapsed):
    positions = set()
    for start_x, start_y, velocity_x, velocity_y in bots:
        end_x, end_y = calculate(start_x, start_y, velocity_x, velocity_y, time_elapsed)
        positions.add((end_x, end_y))
    return positions

def create_grid(positions):
    grid = []
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            if (x, y) in positions:
                row.append('#')
            else:
                row.append('.')
        grid.append(row)
    return grid

def print_grid(grid):
    s = ""
    for row in grid:
        s += "".join(row) + "\n"
    print(s)

def calculate(start_x, start_y, velocity_x, velocity_y, time_elapsed):
    unbounded_x = start_x + velocity_x * time_elapsed
    unbounded_y = start_y + velocity_y * time_elapsed
    end_x = unbounded_x % WIDTH
    end_y = unbounded_y % HEIGHT
    if end_x < 0:
        end_x += WIDTH
    if end_y < 0:
        end_y += HEIGHT
    return end_x, end_y

if __name__ == "__main__":
    main()