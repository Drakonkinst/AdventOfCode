import sys, os, re, math, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    t = 0
    for line in lines:
        n = ints(line)
        m = max(n)
        n.remove(m)
        if n[0] + n[1] > m:
            t += 1
    print(t)

if __name__ == "__main__":
    main()