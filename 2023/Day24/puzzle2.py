import sys, os, itertools as itt
from collections import deque # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
import numpy as np

# https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/ketigrg
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    # Parse input
    hailstones = []
    minVX = 0
    minVY = 0
    minVZ = 0
    for line in lines:
        (px, py, pz, vx, vy, vz) = ints(line)
        minVX = min(minVX, vx)
        minVY = min(minVY, vy)
        minVZ = min(minVZ, vz)
        
        hailstones.append(((px, py, pz), (vx, vy, vz)))
    
    # Shift all velocities to be positive to optimize numpy arrays
    for i in range(len(hailstones)):
        (p, v) = hailstones[i]
        hailstones[i] = (p, (v[0] + minVX, v[1] + minVY, v[2] + minVZ))
    
    # Numpy time!
    # We select three hailstones we assume are linearly independent,
    # which should be all we need to solve with linear algebra.
    
    (p0, v0) = hailstones[0]
    (p1, v1) = hailstones[1]
    (p2, v2) = hailstones[5]
    
    # Ouch my poor rusty math brain
    A = np.array([
        [v1[1] - v0[1], v0[0] - v1[0], 0.0, p0[1] - p1[1], p1[0] - p0[0], 0.0],
        [v2[1] - v0[1], v0[0] - v2[0], 0.0, p0[1] - p2[1], p2[0] - p0[0], 0.0],
        [v1[2] - v0[2], 0.0, v0[0] - v1[0], p0[2] - p1[2], 0.0, p1[0] - p0[0]],
        [v2[2] - v0[2], 0.0, v0[0] - v2[0], p0[2] - p2[2], 0.0, p2[0] - p0[0]],
        [0.0, v1[2] - v0[2], v0[1] - v1[1], 0.0, p0[2] - p1[2], p1[1] - p0[1]],
        [0.0, v2[2] - v0[2], v0[1] - v2[1], 0.0, p0[2] - p2[2], p2[1] - p0[1]]
    ])
    b = [
        (p0[1] * v0[0] - p1[1] * v1[0]) - (p0[0] * v0[1] - p1[0] * v1[1]),
        (p0[1] * v0[0] - p2[1] * v2[0]) - (p0[0] * v0[1] - p2[0] * v2[1]),
        (p0[2] * v0[0] - p1[2] * v1[0]) - (p0[0] * v0[2] - p1[0] * v1[2]),
        (p0[2] * v0[0] - p2[2] * v2[0]) - (p0[0] * v0[2] - p2[0] * v2[2]),
        (p0[2] * v0[1] - p1[2] * v1[1]) - (p0[1] * v0[2] - p1[1] * v1[2]),
        (p0[2] * v0[1] - p2[2] * v2[1]) - (p0[1] * v0[2] - p2[1] * v2[2])
    ]
    solution = np.linalg.solve(A, b)
    #print(solution)
    print(round(solution[0] + solution[1] + solution[2]))
    # Off by 1? Really? I'll just plug in another vector
    
if __name__ == "__main__":
    main()