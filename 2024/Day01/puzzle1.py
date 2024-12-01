import sys, os, itertools as itt
from collections import deque # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    left = []
    right = []
    for line in lines:
        vals = ints(line)
        left.append(vals[0])
        right.append(vals[1])
    left.sort()
    right.sort()
    distances = [abs(left[i] - right[i]) for i in range(len(left))]
    total = sum(distances)
    print(total)

if __name__ == "__main__":
    main()