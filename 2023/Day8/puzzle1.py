import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    instr = lines[0]
    
    m = {}
    for line in lines[2:]:
        w = words(line)
        parent = w[0]
        left = w[2][1:-1]
        right = w[3][:-1]
        m[parent] = (left, right)
    step = 0
    curr = "AAA"
    while curr != "ZZZ":
        i = instr[step % len(instr)]
        if i == "R":
            curr = m[curr][1]
        else:
            curr = m[curr][0]
        step += 1
    print(step)

if __name__ == "__main__":
    main()