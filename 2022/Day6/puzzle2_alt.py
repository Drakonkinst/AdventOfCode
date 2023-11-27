import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

GOAL_LEN = 14

def all_unique(d):
    s = set()
    for c in d:
        if c in s:
            return False
        s.add(c)
    return True
    
def main():
    d = deque()
    line = lines[0]
    for i, c in enumerate(line):
        d.append(c)
        if len(d) > GOAL_LEN:
            d.popleft()
            if all_unique(d):
                print(i + 1)
                return
    print("FAIL")

if __name__ == "__main__":
    main()