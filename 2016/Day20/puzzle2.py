import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    # Read all intervals
    intervals = []
    for line in lines:
        nums = positive_ints(line)
        intervals.append((nums[0], nums[1]))
    intervals.sort()
    
    q = []
    # Compress intervals
    for lo, hi in intervals:
        if len(q) <= 0:
            q.append([lo, hi])
            continue
        currMin = q[-1][0]
        currMax = q[-1][1]
        if lo > currMax + 1:
            q.append([lo, hi])
            continue
        q[-1][1] = max(currMax, hi)
        
    # We know intervals do not overlap because they are
    # compressed, so just accumulate them
    totalPossible = 4294967295 + 1 # From 0 to 4294967295
    totalBlocked = 0
    for lo, hi in q:
        totalBlocked += hi - lo + 1
    print(totalPossible - totalBlocked)

if __name__ == "__main__":
    main()