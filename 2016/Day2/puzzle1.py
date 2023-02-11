import sys, os, re, math, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    k = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    r = 1
    c = 1
    s = ""
    for line in lines:
        for ch in line:
            if ch == "U" and r > 0:
                r -= 1
            elif ch == "L" and c > 0:
                c -= 1
            elif ch == "R" and c < 2:
                c += 1
            elif ch == "D" and r < 2:
                r += 1
        s += str(k[r][c])
    print(s)

if __name__ == "__main__":
    main()