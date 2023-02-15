import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    n = 0
    for line in lines:
        dims = ints(line)
        
        # Calculate surface area
        l, w, h = dims
        surfaceArea = 2*l*w + 2*w*h + 2*l*h
        
        # Find the area of the smallest side
        dims.sort()  # Move longest dimension to the end
        smallestArea = dims[0] * dims[1]
        n += surfaceArea + smallestArea
    print(n)

if __name__ == "__main__":
    main()