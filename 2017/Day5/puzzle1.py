import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    jumps = [int(line) for line in lines]
    jumpIndex = 0
    step = 0
    
    while 0 <= jumpIndex < len(jumps):
        jumpDistance = jumps[jumpIndex]
        jumps[jumpIndex] += 1
        jumpIndex += jumpDistance
        step += 1
    print(step)

if __name__ == "__main__":
    main()