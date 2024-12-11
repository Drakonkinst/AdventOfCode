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
        total += validate_and_fix(order, rules)
        index += 1
    print(total)

def validate_and_fix(initial_order, rules):
    # Time to fix!
    # We'll assume this will end in no infinite loops...
    q = deque()
    q.append(initial_order)
    solution_order = None
    visited = set()
    while len(q):
        order = q.pop()

        # Make sure not to explore the same order twice
        key = " ".join([str(x) for x in order])
        if key in visited:
            continue
        visited.add(key)
        violation = validate(order, rules)

        if violation is None:
            solution_order = order
            break
        before, after = violation
        # We can assume before_index > after_index
        before_index = order.index(before)
        after_index = order.index(after)
        # Attempt to place the first item in all places behind the second
        for i in range(after_index + 1):
            new_order = order[:i] + [before] + order[i:before_index] + order[before_index + 1:]
            assert(len(new_order) == len(initial_order))
            q.append(new_order)

    if solution_order is None:
        # No solution found, shouldn't happen
        assert False
    # Return midpoint of the fixed order
    if initial_order == solution_order:
        # No increment for orders that were already valid
        return 0
    return solution_order[len(solution_order) // 2]


# Return the offending rule, or null if valid
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
            # Invalid! Return the rule
            return rule
    # In the correct order, return
    return None

if __name__ == "__main__":
    main()