import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

# Naive solution
def main():
    patterns = lines[0].split(", ")
    designs = lines[2:]
    total = 0

    for design in designs:
        if is_possible(design, patterns):
            total += 1
    print(total)

def is_possible(design, patterns):
    q = deque()
    q.append(design)
    visited = set()

    while len(q):
        remaining_design = q.pop()
        if remaining_design in patterns:
            return True
        if remaining_design in visited:
            continue
        visited.add(remaining_design)
        for pattern in patterns:
            if remaining_design.startswith(pattern):
                q.append(remaining_design[len(pattern):])

if __name__ == "__main__":
    main()