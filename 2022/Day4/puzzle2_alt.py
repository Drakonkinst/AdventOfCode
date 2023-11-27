import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def any_overlap(a1, a2, b1, b2):
    return (b1 <= a1 <= b2) or (b1 <= a2 <= b2) or (a1 <= b1 <= a2) or (a1 <= b2 <= a2)

def main():
    total = 0
    for line in lines:
        a, b, c, d = positive_ints(line)
        if any_overlap(a, b, c, d):
            total += 1
    print(total)

if __name__ == "__main__":
    main()