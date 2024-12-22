import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

MAX_CHEAT_DISTANCE = 20
def main():
    start_pos = None
    end_pos = None
    walls = set()
    height = len(lines)
    width = len(lines[0])
    for y in range(height):
        for x in range(width):
            ch = lines[y][x]
            if ch == 'S':
                start_pos = (x, y)
            elif ch == 'E':
                end_pos = (x, y)
            elif ch == '#':
                walls.add((x, y))
    assert start_pos is not None and end_pos is not None

    q = deque()
    q.append((0, start_pos, None)) # time, pos, prev_pos
    racetrack = {}
    while len(q):
        time, pos, prev_pos = q.pop()
        racetrack[pos] = time
        if pos == end_pos:
            break
        for offset in CARDINAL_NEIGHBORS:
            next_pos = addT(pos, offset)
            if next_pos in walls or next_pos == prev_pos:
                continue
            q.append((time + 1, next_pos, pos))

    cheat_offsets = build_offsets()
    timesaves = []
    for pos, time in racetrack.items():
        for offset in cheat_offsets:
            next_pos = addT(pos, offset)
            cheat_distance = abs(offset[0]) + abs(offset[1])
            if next_pos in racetrack:
                # Would this have saved more time than if we moved normally?
                next_time = racetrack[next_pos]
                time_saved = next_time - (time + cheat_distance)
                if time_saved >= 100:
                    timesaves.append(time_saved)
    # Print all the timesave frequencies from least to greatest
    # print(sorted(Counter(timesaves).items(), key = lambda e: e[0]))
    print(len(timesaves))


# Offsets of every tile in range of a cheat, that could
def build_offsets():
    offsets = []
    for xOffset in range(-MAX_CHEAT_DISTANCE, MAX_CHEAT_DISTANCE + 1):
        for yOffset in range(-MAX_CHEAT_DISTANCE, MAX_CHEAT_DISTANCE + 1):
            delta = abs(xOffset) + abs(yOffset)
            if delta >= 2 and delta <= MAX_CHEAT_DISTANCE:
                offsets.append((xOffset, yOffset))
    return offsets


if __name__ == "__main__":
    main()