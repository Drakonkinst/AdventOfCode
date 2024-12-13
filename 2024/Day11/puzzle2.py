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
    initial_values = ints(lines[0])
    num_blinks = 75
    result = solve(initial_values, num_blinks)
    print(result)


def solve(values, num_blinks):
    q = deque()
    cache = {}
    for value in values:
        q.append((value, num_blinks))

    while len(q):
        key = q.pop()
        if key in cache:
            continue
        value, num_blinks = key
        next_iteration = blink(value)
        if num_blinks == 1:
            cache[key] = len(next_iteration)
            continue
        total = 0
        missing = []
        for next_value in next_iteration:
            next_key = (next_value, num_blinks - 1)
            if next_key in cache:
                total += cache[next_key]
            else:
                missing.append(next_key)
        if len(missing):
            q.append(key)
            for missing_value in missing:
                q.append(missing_value)
        else:
            cache[key] = total
    # print(cache)

    # Now gather all the initial values
    result = 0
    for value in values:
        key = (value, num_blinks)
        if key not in cache:
            assert False
        result += cache[key]
    return result

def evolve(value, num_blinks):
    key = value + ' ' + num_blinks
    if key in cache:
        return cache[key]

def blink(value):
    if value == 0:
        return [1]
    value_str = str(value)
    num_digits = len(value_str)
    if num_digits % 2 == 0:
        midpoint = num_digits // 2
        first_value = int(value_str[:midpoint])
        second_value = int(value_str[midpoint:])
        return [first_value, second_value]
    return [value * 2024]


if __name__ == "__main__":
    main()