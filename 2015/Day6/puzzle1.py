import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    width = 1000
    height = 1000
    grid = make_grid((width, height), False)
    for line in lines:
        x1, y1, x2, y2 = ints(line)
        
        # Determine operation through first words
        if line.startswith("turn off"):
            op = 0
        elif line.startswith("turn on"):
            op = 1
        elif line.startswith("toggle"):
            op = 2
        else:
            assert False
        
        # Perform operation across range
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if op == 0:
                    # Turn off
                    grid[x][y] = False
                if op == 1:
                    # Turn on
                    grid[x][y] = True
                if op == 2:
                    # Toggle
                    grid[x][y] = not grid[x][y]
    
    # Count all lights 
    n = 0
    for x in range(width):
        for y in range(height):
            if grid[x][y]:
                n += 1
    print(n)

if __name__ == "__main__":
    main()