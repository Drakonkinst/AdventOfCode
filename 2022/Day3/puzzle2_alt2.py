import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

PRIO = LOWERCASE_STR + UPPERCASE_STR

def main():
    total = 0
    for l1, l2, l3 in grouped(lines, 3):
        l1_c = set([c for c in l1])
        l2_c = set([c for c in l2])
        l3_c = set([c for c in l3])
        same = list(set.intersection(l1_c, l2_c, l3_c))
        total += PRIO.index(same[0]) + 1
    print(total)

if __name__ == "__main__":
    main()