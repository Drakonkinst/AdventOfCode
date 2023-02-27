import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

nodes = {}

def viable(coordsA, coordsB):
    if coordsA == coordsB:
        return False
    nodeA = nodes[coordsA]
    nodeB = nodes[coordsB]
    usedA = nodeA[1]
    availB = nodeB[2]
    return usedA > 0 and usedA <= availB
    
def main():
    l = lines[2:]
    for line in l:
        nums = tuple(ints(line))
        x, y, size, used, avail, usePerc = nums
        nodes[(x, y)] = (size, used, avail, usePerc)
    
    total = 0
    for coordsA, coordsB in itt.permutations(nodes.keys(), 2):
        if viable(coordsA, coordsB):
            total += 1
    print(total)

if __name__ == "__main__":
    main()