import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    nums = lines[0]
    i = 1
    firstNum = int(nums[0])
    lastNum = firstNum
    total = 0
    while i < len(nums):
        currNum = int(nums[i])
        if currNum == lastNum:
            total += currNum
        lastNum = currNum
        i += 1
    if lastNum == firstNum:
        total += currNum
    print(total)
    
if __name__ == "__main__":
    main()