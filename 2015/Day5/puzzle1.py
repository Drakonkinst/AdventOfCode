import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    vow = set(["a", "e", "i", "o", "u"])
    lt = set(["ab", "cd", "pq", "xy"])
    n = 0
    for line in lines:
        nv = 0
        ls = ""
        lsFound = False
        ltFound = False
        for i in range(len(line)):
            ch = line[i]
            if ch in vow:
                nv += 1
            if ls == ch:
                lsFound = True
            if i > 0:
                lastTwo = line[i - 1:i + 1]
                if lastTwo in lt:
                    ltFound = True
                    break
            ls = ch
        if lsFound and nv >= 3 and not ltFound:
            n += 1
    print(n)

if __name__ == "__main__":
    main()