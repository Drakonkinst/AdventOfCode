import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    times = ints(lines[0])
    distances = ints(lines[1])
    
    time = int("".join([str(x) for x in times]))
    distance = int("".join([str(x) for x in distances])) + 0.01
    
    # The power of the quadratic formula!
    upper = math.floor((time + math.sqrt(time * time - (4 * distance))) / 2)
    lower = math.ceil((time - math.sqrt(time * time - (4 * distance))) / 2)
        
    ways = upper - lower + 1
    print(ways)

if __name__ == "__main__":
    main()