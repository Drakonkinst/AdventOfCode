import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    for line in lines:
        nums = ints(line)
        diff = max(nums) - min(nums)
        total += diff
    print(total)

if __name__ == "__main__":
    main()