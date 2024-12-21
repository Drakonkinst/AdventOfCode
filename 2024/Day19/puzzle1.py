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
    patterns = lines[0].split(", ")
    designs = lines[2:]
    total = 0

    # Keep a cache of patterns that are known to be solvable (and in how many ways)
    cache = {}

    for design in designs:
        if get_num_ways(design, patterns, cache) > 0:
            total += 1
    print(total)

def get_num_ways(design, patterns, cache):
    if len(design) <= 0:
        return 1
    if design in cache:
        return cache[design]
    num_ways = 0
    for pattern in patterns:
        if not design.startswith(pattern):
            continue
        num_ways += get_num_ways(design[len(pattern):], patterns, cache)
    cache[design] = num_ways
    return num_ways

if __name__ == "__main__":
    main()