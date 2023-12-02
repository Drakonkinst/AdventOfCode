import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    
    blue = 14
    red = 12
    green = 13
    
    for line in lines:
        w = words(line)
        gameId = ints(w[1])[0]
        good = True
        for countStr, colorStr in grouped(w, 2):
            i = ints(countStr)
            if not i:
                continue
            num = i[0]
            if colorStr.startswith("blue"):
                if num > blue:
                    good = False
                    break
            if colorStr.startswith("red"):
                if num > red:
                    good = False
                    break
            if colorStr.startswith("green"):
                if num > green:
                    good = False
                    break
        if good:
            total += gameId
    print(total)

if __name__ == "__main__":
    main()