import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    directions = lines[0]
    n = 0
    i = 0
    while i < len(directions):
        ch = directions[i]
        if ch == '(':
            n += 1
        else:
            n -= 1

        # Check floor
        if n == -1:
            # Output is 1-indexed
            print(i + 1)
            return
        i += 1
    print("FAIL")

if __name__ == "__main__":
    main()