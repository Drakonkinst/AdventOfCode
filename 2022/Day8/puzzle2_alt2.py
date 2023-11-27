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
            
def score(x, y):
    s = 1
    for xo, yo in CARDINAL_NEIGHBORS:
        step = 1
        h = vals[x][y]
        while 0 <= x + xo * step <= width - 1 and 0 <= y + yo * step <= height - 1:
            k = vals[x + xo * step][y + yo * step]
            step += 1
            if k >= h:
                break
        s *= step - 1
    return s

def main():
    maxScore = 0
    for x in range(width):
        for y in range(height):
            maxScore = max(score(x, y), maxScore)
    print(maxScore)

if __name__ == "__main__":
    main()