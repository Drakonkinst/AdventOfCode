import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]
# Up, right, down, left
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def main():
    # Read map
    guard_pos = None
    direction = 0
    obstacles = set()
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            tile = lines[row][col]
            if tile == '#':
                obstacles.add((row, col))
            elif tile == '^':
                guard_pos = (row, col)
    if guard_pos is None:
        assert False

    # Play as guard, stop when you enter the same tile facing the same direction
    visited = set()
    while True:
        key = (guard_pos, direction)
        if key in visited:
            break
        visited.add(key)
        direction_offset = DIRECTIONS[direction]
        ahead_pos = addT(guard_pos, direction_offset)
        if ahead_pos in obstacles:
            # Rotate 90 degrees
            direction = (direction + 1) % len(DIRECTIONS)
        else:
            # Move in target direction
            guard_pos = ahead_pos
            # If out of bounds, it'll never come back. Just stop it there
            if not in_bounds(guard_pos, len(lines), len(lines[0])):
                break
    visited_pos = set([pos for pos, _ in visited])
    print(len(visited_pos))

def print_grid(visited_pos, obstacles, num_rows, num_cols):
    for row in range(num_rows):
        s = ""
        for col in range(num_cols):
            if (row, col) in visited_pos:
                s += "X"
            elif (row, col) in obstacles:
                s += "#"
            else:
                s += "."
        print(s)

if __name__ == "__main__":
    main()