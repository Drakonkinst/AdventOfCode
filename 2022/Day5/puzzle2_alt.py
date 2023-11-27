import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line for line in file.readlines()]

def main():
    i = 0
    width = 0
    data = []
    
    # Read data
    while i < len(lines):
        line = lines[i]
        if line[1].isnumeric():
            break
        row = []
        rowWidth = 0
        for letter in line[1::4]:
            row.append(letter)
            rowWidth += 1
        width = max(width, rowWidth)
        data.append(row)
        i += 1
    
    # Parse data
    blocks = [[] for _ in range(width)]
    for row in data[::-1]:
        for index, item in enumerate(row):
            if item != " ":
                blocks[index].append(item)
    
    # Do instructions
    i += 2
    while i < len(lines):
        a, x, y = ints(lines[i])
        b = blocks[x - 1][-a:]
        blocks[x - 1] = blocks[x - 1][:-a]
        blocks[y - 1].extend(b)
        i += 1
    
    print("".join([b[-1] for b in blocks]))

if __name__ == "__main__":
    main()