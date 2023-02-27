import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

nodes = {}

def viable(coordsA, coordsB, allNodes):
    if coordsA == coordsB:
        return False
    nodeA = allNodes[coordsA]
    nodeB = allNodes[coordsB]
    usedA = nodeA[1]
    availB = nodeB[2]
    return usedA > 0 and usedA <= availB
    
def main():
    l = lines[2:]
    maxX = -1
    for line in l:
        nums = tuple(ints(line))
        x, y, size, used, avail, usePerc = nums
        if y == 0:
            maxX = max(x, maxX)
        nodes[(x, y)] = (size, used, avail, usePerc)
    
    goal = (maxX, 0)
    q = deque()
    for coordsA, coordsB in itt.permutations(nodes.keys(), 2):
        if viable(coordsA, coordsB, nodes):
            q.append((0, coordsA, coordsB, goal, nodes.copy()))
            
    print(len(q))

    lastStep = -1
    while len(q) > 0:
        step, coordsA, coordsB, goal, allNodes = q.popleft()
        if step > lastStep:
            lastStep = step
            print("STEP", step)
        if goal == (0, 0):
            print(step)
            return
        for a, b in itt.permutations(allNodes.keys(), 2):
            if viable(a, b, allNodes):
                if a == goal:
                    goal = b
                q.append((0, a, b, goal, allNodes.copy()))

if __name__ == "__main__":
    main()