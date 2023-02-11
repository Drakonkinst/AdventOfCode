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
        dims.sort()
        per = dims[0] * 2 + dims[1] * 2
        vol = a * b * c
        n += per + vol
    print(n)

if __name__ == "__main__":
    main()