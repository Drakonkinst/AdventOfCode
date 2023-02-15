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
        
        # Move longest dimension to the end
        dims.sort()
        
        # Calculate perimeter of smallest side
        smallestPerimeter = dims[0] * 2 + dims[1] * 2
        
        # Calculate volume for the bow
        volume = dims[0] * dims[1] * dims[2]
        
        n += smallestPerimeter + volume
    print(n)

if __name__ == "__main__":
    main()