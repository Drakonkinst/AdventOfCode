import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    moves = lines[0]
    
    # Keep track of all visited locations
    pos = (0, 0)
    v = set([pos])
    for ch in moves:
        offset = arrow(ch)
        pos = addT(pos, offset)
        v.add(pos)
    
    # Presents delivered is equal to number of unique houses visited
    print(len(v))

if __name__ == "__main__":
    main()