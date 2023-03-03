import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def hash_pois(poisRemaining, pois):
    total = 0
    multiplier = 0
    for poi in pois:
        if poi in poisRemaining:
            total += 2 ** multiplier
        multiplier += 1
    return total

def main():
    start = None
    pois = []
    grid = []
    for y in range(len(lines)):
        line = lines[y]
        row = []
        for x in range(len(line)):
            ch = line[x]
            if ch == "#":
                row.append(False)
            elif ch == ".":
                row.append(True)
            elif ch == "0":
                row.append(True)
                start = (x, y)
            else:
                row.append(True)
                pois.append((x, y))
        grid.append(row)
    
    q = deque([(0, start, pois, [])])
    v = set()
    lastStep = -1
    while len(q) > 0:
        step, currPos, poisRemaining, poiOrder = q.popleft()
        currX, currY = currPos
        
        state = (currPos, hash_pois(poisRemaining, pois))
        if state in v:
            continue
        v.add(state)
        
        if step > lastStep:
            lastStep = step
            print("Step", step)

        if len(poisRemaining) <= 0:
            print(step, currPos, poiOrder)
            # This needs a -1 for some reason. I'm not sure why.
            print("ANS", step - 1)
            return
        
        if currPos in poisRemaining:
            poisRemaining = poisRemaining.copy()
            poisRemaining.remove(currPos)
            poiOrder = poiOrder.copy()
            poiOrder.append(currPos)
        
        #print(step, currPos, poiOrder)

        for xOffset, yOffset in CARDINAL_NEIGHBORS:
            x = currX + xOffset
            y = currY + yOffset
            if grid[y][x]:
                q.append((step + 1, (x, y), poisRemaining, poiOrder))
    print("FAIL")

if __name__ == "__main__":
    main()