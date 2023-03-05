import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

# A math-based solution that finds the answer super quickly
def main():
    target = int(lines[0])
    
    i = 1
    while True:
        if i * i >= target:
            i -= 2
            break
        i += 2
        
    ring = i // 2 + 1
        
    # Calculate bounds
    corners = [(1, -1), (-1, -1), (-1, 1), (1, 1)]
    dirs = [DOWN, RIGHT, UP, LEFT]
    
    # Get offset along ring
    distanceOnRing = target - 1 - i * i
    pos = None
    for j in range(4):
        corner = (j + 1) * (2 * ring)
        if distanceOnRing < corner:
            distanceFromCorner = corner - 1 - distanceOnRing
            pos = addT(smultT(corners[j], ring), smultT(dirs[j], distanceFromCorner))
            break
    manhattanDistance = abs(pos[0]) + abs(pos[1])
    print(manhattanDistance)

if __name__ == "__main__":
    main()