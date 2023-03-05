import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    nums = [int(ch) for ch in lines[0]]
    i = 0
    total = 0
    while i < len(nums):
        j = (i + (len(nums) // 2)) % len(nums)
        if nums[i] == nums[j]:
            total += nums[i]
        i += 1
    print(total)

if __name__ == "__main__":
    main()