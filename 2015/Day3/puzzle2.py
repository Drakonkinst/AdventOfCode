import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    v = set()
    pos = (0, 0)
    pos2 = (0, 0)
    v.add(pos)
    n = 1
    turn = False
    for ch in lines[0]:
        if turn:
            pos = addT(pos, arrow(ch))
            if pos not in v:
                n += 1
            v.add(pos)
        else:
            pos2 = addT(pos2, arrow(ch))
            if pos2 not in v:
                n += 1
            v.add(pos2)
        turn = not turn
    print(n)

if __name__ == "__main__":
    main()