import sys, os, itertools as itt
from collections import deque # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def det(p1, p2):
    return p1[0] * p2[1] - p2[0] * p1[1]

# https://stackoverflow.com/questions/20677795
def get_intersection(a, b):
    (ap, av) = a
    (bp, bv) = b
    xdiff = (-av[0], -bv[0])
    ydiff = (-av[1], -bv[1])
    div = det(xdiff, ydiff)
    if div == 0:
        return (-1, -1, False)
    ap2 = addT(ap, av)
    bp2 = addT(bp, bv)
    d = (det(ap, ap2), det(bp, bp2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    
    if ((ap[0] > x) == (av[0] > 0)) and ((ap[1] > y) == (av[1] > 0)):
        return (x, y, False)
    if ((bp[0] > x) == (bv[0] > 0)) and ((bp[1] > y) == (bv[1] > 0)):
        return (x, y, False)
    
    return (x, y, True)

def main():
    # Example
    xMin = 7
    xMax = 27
    # Part 1
    xMin = 200000000000000
    xMax = 400000000000000
    
    yMin = xMin
    yMax = xMax
    
    hailstones = []
    for line in lines:
        (px, py, pz, vx, vy, vz) = ints(line)
        #hailstones.append(((px, py, pz), (vx, vy, vz)))
        hailstones.append(((px, py), (vx, vy)))
    
    total = 0
    for (a, b) in itt.combinations(hailstones, 2):
        p = get_intersection(a, b)
        #print(a, b, p)
        valid = p[2]
        if not valid:
            continue
        if xMin <= p[0] <= xMax and yMin <= p[1] <= yMax:
            total += 1
    print(total)

if __name__ == "__main__":
    main()