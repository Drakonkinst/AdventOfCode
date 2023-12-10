import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def get_nums(original):
    nums = []
    nums.append(original)
    while True:
        allZero = True
        nextNums = []
        for i in range(len(nums[-1]) - 1):
            diff = nums[-1][i + 1] - nums[-1][i]
            if diff != 0:
                allZero = False
            nextNums.append(diff)
        nums.append(nextNums)
        if allZero:
            break
    return nums

def extrapolate(nums):
    for numList in nums:
        numList.append(0)
    for level in range(len(nums) - 2, -1, -1):
        nums[level][-1] = nums[level][-2] + nums[level + 1][-1]
    return nums[0][-1]
    
def main():
    total = 0
    for line in lines:
        nums = get_nums(ints(line))
        ext = extrapolate(nums)
        total += ext
    print(total)

if __name__ == "__main__":
    main()