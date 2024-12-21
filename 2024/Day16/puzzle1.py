import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

COST_STEP = 1
COST_TURN = 1000
def main():
    walls = set()
    start_pos = None
    end_pos = None
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            ch = line[x]
            if ch == '#':
                walls.add((x, y))
            elif ch == 'S':
                start_pos = (x, y)
            elif ch == 'E':
                end_pos = (x, y)
    assert start_pos is not None and end_pos is not None

    q = PriorityQueue()
    q.put((0, start_pos, RIGHT))
    visited = set()
    while q:
        cost, pos, direction = q.get()
        key = (pos, direction)
        if key in visited:
            continue
        if pos == end_pos:
            print(cost)
            return
        visited.add(key)
        ahead_pos = addT(pos, direction)
        if ahead_pos not in walls:
            q.put((cost + COST_STEP, ahead_pos, direction))
        current_direction_index = CARDINAL_NEIGHBORS.index(direction)
        counterclockwise = CARDINAL_NEIGHBORS[(current_direction_index - 1 + len(CARDINAL_NEIGHBORS)) % len(CARDINAL_NEIGHBORS)]
        clockwise = CARDINAL_NEIGHBORS[(current_direction_index + 1) % len(CARDINAL_NEIGHBORS)]
        q.put((cost + COST_TURN, pos, counterclockwise))
        q.put((cost + COST_TURN, pos, clockwise))


if __name__ == "__main__":
    main()