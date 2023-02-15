import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    n = 0
    for line in lines:
        doublePairFound = False
        xyxFound = False
        pairs = {}
        for i in range(len(line)):
            ch = line[i]
            
            # Check for double pair
            if i >= 1:
                lastPair = line[i - 1] + ch
                # If pair is already found and does not overlap
                if lastPair in pairs and pairs[lastPair] < i - 1:
                    doublePairFound = True
                pairs[lastPair] = i
            
            # Check for xyx pattern
            if i >= 2:
                # y value does not matter
                if line[i - 2] == ch:
                    xyxFound = True
            lastChar = ch
        if doublePairFound and xyxFound:
            n += 1
    print(n)

if __name__ == "__main__":
    main()