import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    numRows = 6
    numCols = 50
    grid = make_grid((numRows, numCols), 0)

    for line in lines:
        vals = ints(line)
        if line.startswith("rect"):
            width = vals[0]
            height = vals[1]
            for c in range(0, width):
                for r in range(0, height):
                    grid[r][c] = 1
        elif line.startswith("rotate row"):
            row = vals[0]
            dist = vals[1]
            newRow = [-1] * numCols
            for i in range(numCols):
                newIndex = (i + dist) % numCols
                newRow[newIndex] = grid[row][i]
            for i in range(numCols):
                grid[row][i] = newRow[i]    
        elif line.startswith("rotate column"):
            col = vals[0]
            dist = vals[1]
            newCol = [-1] * numRows
            for i in range(numRows):
                newIndex = (i + dist) % numRows
                newCol[newIndex] = grid[i][col]
            for i in range(numRows):
                grid[i][col] = newCol[i] 
    for row in grid:
        print("".join(["#" if x == 1 else "." for x in row]))

if __name__ == "__main__":
    main()