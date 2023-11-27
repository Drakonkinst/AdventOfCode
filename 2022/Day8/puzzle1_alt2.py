import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

width = len(lines)
height = len(lines[0])

# Read grid
vals = make_grid((width, height))
for x in range(width):
    for y in range(height):
        vals[x][y] = lines[x][y]
            
def check(x, y):
    for xo, yo in CARDINAL_NEIGHBORS:
        step = 1
        canSee = True
        h = vals[x][y]
        while 0 <= x + xo * step <= width - 1 and 0 <= y + yo * step <= height - 1:
            k = vals[x + xo * step][y + yo * step]
            if k >= h:
                canSee = False
                break
            step += 1
        if canSee:
            return True
    return False

def main():
    total = 0
    for x in range(width):
        for y in range(height):
            if check(x, y):
                total += 1
    print(total)

if __name__ == "__main__":
    main()