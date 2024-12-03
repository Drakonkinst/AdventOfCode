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
    instructions = dos_and_donts(lines)
    for line in instructions:
        total += get_line_total(line)
    print(total)

# Remove all sections of disabled code ahead of time
# To ensure combined sections do not accidentally concatenate partial instructions,
# make them separate lines
def dos_and_donts(lines):
    instructions = []
    enabled = True # Enabled at the beginning of the program, not each line!
    for line in lines:
        index = 0
        while index < len(line):
            # When enabled, we only care about when the next disable is, and vice versa
            if enabled:
                # Thank goodness this isn't regex by default
                next_disable = line.find("don't()", index)
                if next_disable < 0:
                    instructions.append(line[index:])
                    break
                instructions.append(line[index:next_disable])
                index = next_disable + len("don't()")
                enabled = False
            else:
                next_enable = line.find("do()", index)
                if next_enable < 0:
                    break
                index = next_enable + len("do()")
                enabled = True
    return instructions

def get_line_total(line):
    index = 0
    total = 0
    while index < len(line):
        next_mul = line.find("mul(", index)
        if next_mul < 0:
            break
        result, next_index = parse_mul(line, next_mul)
        index = next_index
        total += result
    return total

MAX_LENGTH = 3

# We assume that all numbers are positive and at most 3 digits
def parse_mul(line, index):
    index += len("mul(")

    # First number
    first_num_str = ""
    while True:
        next_char = line[index]
        index += 1
        if next_char in DIGITS:
            if len(first_num_str) >= MAX_LENGTH:
                return (0, index)
            first_num_str += next_char
        elif next_char == ',':
            break
        else:
            return (0, index)

    # Second number
    second_num_str = ""
    while True:
        next_char = line[index]
        index += 1
        if next_char in DIGITS:
            if len(second_num_str) >= MAX_LENGTH:
                return (0, index)
            second_num_str += next_char
        elif next_char == ')':
            break
        else:
            return (0, index)
    result = parse_int(first_num_str) * parse_int(second_num_str)
    return (result, index)

if __name__ == "__main__":
    main()