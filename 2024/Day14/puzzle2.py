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

    i = 0
    while True:
        positions = get_positions(bots, i)
        i += 1
        quadrants = [0, 0, 0, 0]
        for position in positions:
            quadrant = get_quadrant(position[0], position[1])
            quadrants[quadrant] += 1
        if i % 1000 == 0:
            print("Searching", i)
        if not (quadrants[0] == quadrants[1] and quadrants[2] == quadrants[3]):
            continue
        print("PASS")
        grid = create_grid(positions)

        # if is_symmetric(grid):
        print_grid(positions)
        print(i, quadrants)

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
def print_grid(positions):
    grid = create_grid(positions)
    s = ""
    for row in grid:
        s += "".join(row) + "\n"
    print(s)

def is_symmetric(grid):
    for row in grid:
        for i in range(len(row) // 2):
            start_index = i
            end_index = len(row) - i - 1
            if row[start_index] != row[end_index]:
                return False
    return True

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

def get_quadrant(end_x, end_y):
    middle_width = WIDTH // 2
    middle_height = HEIGHT // 2
    if end_x == middle_width or end_y == middle_height:
        return -1
    quadrant_x = 0 if end_x < middle_width else 1
    quadrant_y = 0 if end_y < middle_height else 1
    return encode_quadrant(quadrant_x, quadrant_y)

def encode_quadrant(quadrant_x, quadrant_y):
    return quadrant_y * 2 + quadrant_x

if __name__ == "__main__":
    main()