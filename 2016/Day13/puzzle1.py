import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]
favNum = int(lines[0])

def isWall(x, y):
    val = x*x + 3*x + 2*x*y + y + y*y + favNum
    binaryVal = bin(val)[2:]
    numOnes = 0
    for bit in binaryVal:
        if bit == "1":
            numOnes += 1
    return numOnes % 2 != 0

def main():
    goalX = 31
    goalY = 39
    startX = 1
    startY = 1
    
    q = deque([(0, startX, startY)])
    v = set([(startX, startY)])
    while len(q) > 0:
        step, x, y = q.popleft()
        
        if x == goalX and y == goalY:
            print("ANS", step)
            return
        
        for xOffset, yOffset in CARDINAL_NEIGHBORS:
            neighborX = x + xOffset
            neighborY = y + yOffset
            
            if neighborX < 0 or neighborY < 0 or isWall(neighborX, neighborY) or (neighborX, neighborY) in v:
                continue
            q.append((step + 1, neighborX, neighborY))
            v.add((neighborX, neighborY))
    print("FAIL")

if __name__ == "__main__":
    main()