import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    v = set()
    x = 0
    y = 0
    v.add((x, y))
    n = 1
    for ch in lines[0]:
        if ch == 'v':
            y += 1
        elif ch == '^':
            y -= 1
        elif ch == '>':
            x += 1
        elif ch == '<':
            x -= 1
        if (x, y) not in v:
            n += 1
        v.add((x, y))
    print(n)

if __name__ == "__main__":
    main()