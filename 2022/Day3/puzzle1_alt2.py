import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

PRIO = LOWERCASE_STR + UPPERCASE_STR

def main():
    total = 0
    for line in lines:
        mid = len(line) // 2
        first = line[:mid]
        second = line[mid:]
        first_c = set([c for c in first])
        for c in second:
            if c in first_c:
                total += PRIO.index(c) + 1
                break
    print(total)

if __name__ == "__main__":
    main()