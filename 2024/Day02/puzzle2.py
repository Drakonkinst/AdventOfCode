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
    total = 0
    for line in lines:
        report = ints(line)
        if is_safe_with_dampening(report):
            total += 1
    print(total)

def is_safe_with_dampening(original_report):
    q = deque()
    q.append((True, original_report))
    while len(q) > 0:
        can_remove, report = q.pop()
        if is_safe(report):
            return True
        elif can_remove:
            # Need to try removing all of them, since it's not clear which is causing the problem
            for i in range(len(report)):
                # Create a copy of that report with that element removed
                modified_report = report[:i] + report[i+1:]
                q.append((False, modified_report))
    return False

# Return bad index, or -1 if good
def is_safe(report):
    if len(report) < 2:
        return True
    prev_level = report[0]
    prev_diff = 0
    for i in range(1, len(report)):
        # Get data
        next_level = report[i]
        diff = next_level - prev_level

        # Calculate
        if diff == 0 or diff * prev_diff < 0:
            # Differences have a different sign or did not change
            return False
        if not (1 <= abs(diff) <= 3):
            # Difference is too far
            return False

        # Next
        prev_diff = diff
        prev_level = next_level
    return True

if __name__ == "__main__":
    main()