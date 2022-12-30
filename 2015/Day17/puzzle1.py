import sys, os, re, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def findIndexLessEqualThan(arr, n, start):
    lo = start
    hi = len(arr) - 1
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] > n:
            lo = mid + 1
        else:
            ans = mid
            hi = mid - 1
    return ans

def main():
    nums = []
    for line in lines:
        nums.append(int(line))
    nums.sort()
    nums = nums[::-1]
    
    n = 150
    q = deque()
    for i in range(len(nums)):
        q.append(([nums[i]], i))
    
    c = 0
    cArrs = []
    while len(q) > 0:
        arr, i = q.pop()
        s = sum(arr)
        if s > n:
            continue
        if s == n:
            c += 1
            cArrs.append(arr)
            continue
        j = findIndexLessEqualThan(nums, n - s, i + 1)
        if j > -1:
            for k in range(j, len(nums)):
                copy = arr.copy()
                copy.append(nums[k])
                q.append((copy, k))
    
    print("ANS", c)

if __name__ == "__main__":
    main()