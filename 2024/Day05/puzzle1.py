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
    # Read the rules
    rules = []
    index = 0
    for line in lines:
        # Stop after blank line
        if not line:
            break
        before, after = ints(line)
        rules.append((before, after))
        index += 1
    index += 1

    total = 0
    while index < len(lines):
        line = lines[index]
        order = ints(line)
        total += validate(order, rules)
        index += 1
    print(total)

def validate(order, rules):
    for rule in rules:
        before, after = rule
        # The lists are small enough that we can afford to do some linear searches here
        try:
            # We can assume each ID is unique in the list, so this should always work
            before_index = order.index(before)
            after_index = order.index(after)
        except ValueError:
            # Either index does not exist, carry on
            continue
        if not (before_index < after_index):
            # Invalid
            return 0
    # Valid, return the middle
    return order[len(order) // 2]

if __name__ == "__main__":
    main()