import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]
blocks = ints(lines[0])

def do_op():
    maxIndex, maxValue = max_index(blocks)
    toAll = maxValue // len(blocks)
    blocks[maxIndex] = 0
    for i in range(len(blocks)):
        blocks[i] += toAll

    remaining = maxValue % len(blocks)
    index = maxIndex
    while remaining > 0:
        index = (index + 1) % len(blocks)
        blocks[index] += 1
        remaining -= 1

def main():
    step = 0
    visited = set()
    visited.add(tuple(blocks))
    target = None
    
    while True:
        step += 1
        do_op()
        t = tuple(blocks)
        if t in visited:
            target = t
            break
        visited.add(t)
    curr = step
    
    while True:
        step += 1
        do_op()
        t = tuple(blocks)
        if t == target:
            break
    print(step - curr)
        

if __name__ == "__main__":
    main()