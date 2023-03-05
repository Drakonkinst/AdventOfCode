import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

# A math-based solution that finds the answer super quickly
def main():
    target = int(lines[0])
    
    ring = 0
    ringStart = 1
    ringEnd = 1
    while True:
        ringWidth = 2 * ring + 1
        ringSize = 8 * ring
        ringStart = ringEnd + 1
        ringEnd += ringSize
        if target <= ringEnd:
            # The target is in this ring
            if ring == 0:
                print(0)
                return
            
            # Starts at an offset (ring, ring) from the center
            # which is exactly 1 step from the spiral's lower-right
            offset = (ring, ring - 1)
            x = ring
            y = ring - 1
            # Calculate bounds
            ringLowerRight = addT(offset, (0, 1))
            ringUpperRight = subT(ringLowerRight, (0, ringWidth - 1))
            ringLowerLeft = subT(ringLowerRight, (ringWidth - 1, 0))
            ringUpperLeft = subT(ringLowerRight, (ringWidth - 1, ringWidth - 1))
            
            # Get offset along ring
            distanceOnRing = target - ringStart
            # Check ringWidth - 1 on each side to prevent overlaps
            checkWidth = ringWidth - 1
            if distanceOnRing < checkWidth:
                # Right side, excluding lower right corner
                distanceOnEdge = distanceOnRing
                distanceFromCorner = checkWidth - 1 - distanceOnEdge
                pos = addT(ringUpperRight, smultT(DOWN, distanceFromCorner))
            elif distanceOnRing < 2 * checkWidth:
                # Top side, excluding upper right corner
                distanceOnEdge = distanceOnRing - checkWidth
                distanceFromCorner = checkWidth - 1 - distanceOnEdge
                pos = addT(ringUpperLeft, smultT(RIGHT, distanceFromCorner))
            elif distanceOnRing < 3 * checkWidth:
                # Left side, excluding upper left corner
                distanceOnEdge = distanceOnRing - 2 * checkWidth
                distanceFromCorner = checkWidth - 1 - distanceOnEdge
                pos = addT(ringLowerLeft, smultT(UP, distanceFromCorner))
            else:
                # Bottom side, excluding lower left corner
                distanceOnEdge = distanceOnRing - 3 * checkWidth
                distanceFromCorner = checkWidth - 1 - distanceOnEdge
                pos = addT(ringLowerRight, smultT(LEFT, distanceFromCorner))
            # Calculate distance
            manhattanDistance = abs(pos[0]) + abs(pos[1])
            print(manhattanDistance)
            return
        ring += 1

if __name__ == "__main__":
    main()