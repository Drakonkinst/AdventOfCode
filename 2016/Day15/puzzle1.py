import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]
discs = []

def is_valid(time):
    for name, size, initialPos in discs:
        # Name can be used to determine falling time
        if (name + initialPos + time) % size != 0:
            return False
    return True

def main():
    # Read input
    cycle = 1
    for line in lines:
        nums = ints(line)
        name = nums[0]
        size = nums[1]
        initialPos = nums[3]
        cycle *= size
        discs.append((name, size, initialPos))
    
    firstTime = 0
    while not is_valid(firstTime):
        firstTime += 1
    print(firstTime)

if __name__ == "__main__":
    main()