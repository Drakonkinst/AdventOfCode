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
gears = {}

def process_num(row, col, numStr):
    if not numStr:
        return
    startCol = col - len(numStr)
    endCol = col - 1
    for neighborRow in range(row - 1, row + 2):
        for neighborCol in range(startCol - 1, endCol + 2):
            if 0 <= neighborRow < numRows and 0 <= neighborCol < numCols:
                neighborCh = data[neighborRow][neighborCol]
                if neighborCh == "*":
                    coords = (neighborRow, neighborCol)
                    if coords not in gears:
                        gears[coords] = []
                    gears[coords].append(int(numStr))

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
                process_num(row, col, numStr)
                numStr = ""
            col += 1
        process_num(row, col, numStr)
        row += 1
    
    for k in gears:
        if len(gears[k]) == 2:
            total += gears[k][0] * gears[k][1]
    print(total)

if __name__ == "__main__":
    main()