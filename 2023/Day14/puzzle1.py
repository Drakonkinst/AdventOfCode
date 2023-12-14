import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    grid = []
    for line in lines:
        grid.append(line)
    grid = rot_90(rot_90(rot_90(grid)))
    
    for row in grid:
        index = 0
        while index < len(row):
            ch = row[index]
            if ch == ".":
                nextFall = index
                while index < len(row):
                    if row[index] == "O":
                        row[index] = "."
                        row[nextFall] = "O"
                        total += len(row) - nextFall
                        index = nextFall
                        break
                    if row[index] == "#":
                        break
                    index += 1
            elif ch == "O":
                total += len(row) - index
            elif ch == "#":
                pass
                    
            index += 1
    print(total)

if __name__ == "__main__":
    main()