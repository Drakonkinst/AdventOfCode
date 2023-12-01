import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    for line in lines:
        nums = positive_ints(line)
        firstDigit = str(nums[0])[0]
        lastDigit = str(nums[-1])[-1]
        total += int(firstDigit + lastDigit)
    print(total)

if __name__ == "__main__":
    main()