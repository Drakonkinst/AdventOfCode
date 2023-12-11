import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    galaxies = []
    emptyRows = []
    emptyCols = [j for j in range(len(lines[0]))]
    for i in range(len(lines)):
        line = lines[i]
        empty = True
        for j in range(len(line)):
            ch = line[j]
            if ch == "#":
                galaxies.append((i, j))
                if j in emptyCols:
                    emptyCols.remove(j)
                empty = False
        if empty:
            emptyRows.append(i)
    
    galaxies.sort(key=lambda x:x[0])
    
    # Shift galaxies
    galaxies.sort(key=lambda x:x[0])
    row = 0
    rowShift = 0
    galaxyIndex = 0
    maxRow = len(lines)
    while row < maxRow:
        if row in emptyRows:
            rowShift += 1000000 - 1
            maxRow += 1
        while galaxyIndex < len(galaxies) and galaxies[galaxyIndex][0] <= row:
            galaxy = galaxies[galaxyIndex]
            galaxies[galaxyIndex] = (galaxy[0] + rowShift, galaxy[1])
            galaxyIndex += 1
        row += 1
    
    galaxies.sort(key=lambda x:x[1])
    col = 0
    colShift = 0
    galaxyIndex = 0
    maxCol = len(lines[0])
    while col < maxCol:
        if col in emptyCols:
            colShift += 1000000 - 1
            maxCol += 1
        while galaxyIndex < len(galaxies) and galaxies[galaxyIndex][1] <= col:
            galaxy = galaxies[galaxyIndex]
            galaxies[galaxyIndex] = (galaxy[0], galaxy[1] + colShift)
            galaxyIndex += 1
        col += 1
        
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            if i == j:
                continue
            distance = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
            total += distance
    print(total)
            

if __name__ == "__main__":
    main()