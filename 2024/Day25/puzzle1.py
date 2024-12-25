import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

ENTRY_HEIGHT = 7
LOCK_WIDTH = 5
AVAILABLE_SPACE = ENTRY_HEIGHT - 2
def main():
    total = 0
    index = 0
    keys = []
    locks = []
    while index < len(lines):
        is_lock = is_all_filled(lines[index])
        heights = []
        for i in range(LOCK_WIDTH):
            heights.append(0)
        for i in range(AVAILABLE_SPACE):
            row = lines[index + i + 1]
            for j in range(len(row)):
                if row[j] == '#':
                    heights[j] += 1
        if is_lock:
            locks.append(heights)
        else:
            keys.append(heights)
        index += ENTRY_HEIGHT + 1

    total = 0
    for key in keys:
        for lock in locks:
            if fits(key, lock):
                total += 1
    print(total)

def is_all_filled(row):
    for ch in row:
        if ch != '#':
            return False
    return True

def fits(key, lock):
    for i in range(len(key)):
        k = key[i]
        l = lock[i]
        if k + l > AVAILABLE_SPACE:
            return False
    return True

if __name__ == "__main__":
    main()