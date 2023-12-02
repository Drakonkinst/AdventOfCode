import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    
    for line in lines:
        w = words(line)
        maxBlue = 0
        maxRed = 0
        maxRed = 0
        for countStr, colorStr in grouped(w, 2):
            i = ints(countStr)
            if not i:
                continue
            num = i[0]
            if colorStr.startswith("blue"):
                maxBlue = max(maxBlue, num)
            if colorStr.startswith("red"):
                maxRed = max(maxRed, num)
            if colorStr.startswith("green"):
                maxRed = max(maxRed, num)
        total += maxBlue * maxRed * maxRed
    print(total)

if __name__ == "__main__":
    main()