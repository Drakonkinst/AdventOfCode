import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    n = 0
    for line in lines:
        dims = ints(line)
        a, b, c = dims
        sa = 2 * a * b + 2 * b * c + 2 * a * c
        
        dims.sort()
        ex = dims[0] * dims[1]
        n += sa + ex
    print(n)

if __name__ == "__main__":
    main()