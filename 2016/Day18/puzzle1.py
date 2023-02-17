import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

# True is trap, False is safe
def getTraps(lastRow):
    i = 0
    nextRow = []
    while i < len(lastRow):
        left = False if (i - 1 < 0) else lastRow[i - 1]
        center = lastRow[i]
        right = False if (i + 1 >= len(lastRow)) else lastRow[i + 1]
        result = isTrap(left, center, right)
        nextRow.append(result)
        i += 1
    return nextRow

def isTrap(left, center, right):
    return left != right
    
def getSafe(row):
    n = 0
    for tile in row:
        if not tile:
            n += 1
    return n

def rowToStr(row):
    return "".join(["^" if x else "." for x in row])

    
def main():
    n = 40
    firstRow = [True if ch == "^" else False for ch in lines[0]]
    numSafe = getSafe(firstRow)
    
    currentRow = firstRow
    i = 1
    while i < n:
        i += 1
        currentRow = getTraps(currentRow)
        numSafeInRow = getSafe(currentRow)
        numSafe += numSafeInRow
    print(numSafe)
    

if __name__ == "__main__":
    main()