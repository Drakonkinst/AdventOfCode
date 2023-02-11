import sys, os, re, math, hashlib, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    p = lines[0]
    
    n = 8
    i = 0
    j = 0
    a = ["?"] * 8
    while j < n:
        while True:
            s = p + str(i)
            i += 1
            h = hashlib.md5(s.encode()).hexdigest()
            if h.startswith("00000"):
                nums = ints(h[5])
                if len(nums) <= 0:
                    continue
                k = int(nums[0])
                if k < 0 or k > 7 or a[k] != "?":
                    continue
                a[k] = h[6]
                print("".join(a))
                j += 1
                break
    print("".join(a))
        
if __name__ == "__main__":
    main()