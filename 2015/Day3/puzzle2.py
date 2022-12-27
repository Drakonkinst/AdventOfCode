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
    x2 = 0
    y2 = 0
    v.add((x, y))
    n = 1
    turn = False
    for ch in lines[0]:
        if turn:
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
        else:
            if ch == 'v':
                y2 += 1
            elif ch == '^':
                y2 -= 1
            elif ch == '>':
                x2 += 1
            elif ch == '<':
                x2 -= 1
            if (x2, y2) not in v:
                n += 1
            v.add((x2, y2))
        turn = not turn
    print(n)

if __name__ == "__main__":
    main()