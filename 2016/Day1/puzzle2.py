import sys, os, re, math, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    moves = lines[0].split(", ")
    x = 0
    y = 0
    f = 0
    
    v = set([(0, 0)])
    for m in moves:
        if m[0] == "R":
            f = (f + 1) % len(CARDINAL_NEIGHBORS)
        elif m[0] == "L":
            f = (f - 1 + len(CARDINAL_NEIGHBORS)) % len(CARDINAL_NEIGHBORS)
        ff = CARDINAL_NEIGHBORS[f]
        d = ints(m)[0]
        for i in range(d):
            x += ff[0]
            y += ff[1]
            if (x, y) in v:
                print(abs(x) + abs(y))
                return
            v.add((x, y))
    print("FAIL")

if __name__ == "__main__":
    main()