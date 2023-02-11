import sys, os, re, math, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def in_bounds(r, c):
    return abs(r - 2) + abs(c - 2) <= 2

def main():
    k = [
        [None, None, 1, None, None],
        [None, 2, 3, 4, None],
        [5, 6, 7, 8, 9],
        [None, "A", "B", "C", None],
        [None, None, "D", None, None]
    ]
    r = 2
    c = 0
    s = ""
    for line in lines:
        for ch in line:
            if ch == "U" and in_bounds(r - 1, c):
                r -= 1
            elif ch == "L" and in_bounds(r, c - 1):
                c -= 1
            elif ch == "R" and in_bounds(r, c + 1):
                c += 1
            elif ch == "D" and in_bounds(r + 1, c):
                r += 1
        if(k[r][c] == None):
            print("FAIL", r, c)
            return
        s += str(k[r][c])
    print(s)

if __name__ == "__main__":
    main()