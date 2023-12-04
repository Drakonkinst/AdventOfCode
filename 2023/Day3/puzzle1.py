import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]
data = []
for line in lines:
    data.append([ch for ch in line])
numRows = len(data)
numCols = len(data[0])

def calc_num_str(row, col, numStr):
    if not numStr:
        return 0
    startCol = col - len(numStr)
    endCol = col - 1
    isPartNumber = False
    for neighborRow in range(row - 1, row + 2):
        for neighborCol in range(startCol - 1, endCol + 2):
            if 0 <= neighborRow < numRows and 0 <= neighborCol < numCols:
                neighborCh = data[neighborRow][neighborCol]
                if neighborCh not in DIGITS and neighborCh != ".":
                    isPartNumber = True
                    break
    if isPartNumber:
        val = int(numStr)
        return val

def main():
    total = 0
    row = 0
    while row < numRows:
        col = 0
        numStr = ""
        while col < numCols:
            ch = lines[row][col]
            if ch in DIGITS:
                numStr += ch
            else:
                total += calc_num_str(row, col, numStr)
                numStr = ""
            col += 1
        total += calc_num_str(row, col, numStr)
        row += 1
    print(total)

if __name__ == "__main__":
    main()