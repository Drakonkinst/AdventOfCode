import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

WIDTH = 70 + 1
# WIDTH = 6 + 1
def main():
    grid = make_grid((WIDTH, WIDTH), None)
    falling_time = 0
    for line in lines:
        (x, y) = ints(line)
        falling_time += 1
        if grid[y][x] is None:
            grid[y][x] = falling_time

    start_pos = (0, 0)
    end_pos = (WIDTH - 1, WIDTH - 1)
    FIXED_TIME = 1024
    # FIXED_TIME = 12
    # print_grid(grid, FIXED_TIME)
    q = deque()
    q.append((0, start_pos))
    visited = set()
    while len(q):
        step, pos = q.popleft()
        if pos in visited:
            continue
        visited.add(pos)

        if pos == end_pos:
            print(step)
            return

        for offset in CARDINAL_NEIGHBORS:
            next_pos = addT(pos, offset)
            if not in_bounds(next_pos, WIDTH, WIDTH):
                continue
            falling_time = grid[next_pos[1]][next_pos[0]]
            # Check if byte has fallen
            if falling_time is not None and falling_time <= FIXED_TIME:
                continue
            q.append((step + 1, next_pos))
    # No way out :(
    assert False

def print_grid(grid, time):
    s = ""
    for y in range(WIDTH):
        for x in range(WIDTH):
            falling_time = grid[y][x]
            if falling_time is not None and falling_time < time:
                s += "#"
            else:
                s += "."
        s += "\n"
    print(s)

if __name__ == "__main__":
    main()