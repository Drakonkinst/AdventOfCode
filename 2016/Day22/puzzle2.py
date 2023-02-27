import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *
from copy import deepcopy

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

# This final solution makes a few assumptions, as tips from the Reddit thread:
# First, "walls" with a large amount of data can neither be moved into or out of
# Second, there is only one blank tile and it is the only tile that can be moved.
# These simplifications make the solution very, very, fast.
# Keeping previous attempts at a more general solution in other files.
nodes = {}
walls = set()

# Hardcoding these to the input

width = 31
height = 34
wallThreshold = 100

# width = 3
# height = 3
# wallThreshold = 20

def is_valid(node):
    x, y = node
    return 0 <= x < height and 0 <= y < width and (x, y) not in walls

# I messed up my x and y somewhere along the line
# and it's too late now
def print_grid(goalPos, blankPos):
    for x in range(height):
        s = ""
        for y in range(width):
            if (x, y) in walls:
                s += "# "
            elif (x, y) == goalPos:
                s += "G "
            elif (x, y) == blankPos:
                s += "_ "
            else:
                s += ". "
        print(s)
            
def main():
    l = lines[2:]
    goal = (height - 1, 0)
    blank = None
    nodeList = []
    for line in l:
        nums = tuple(ints(line))
        x, y, size, used, avail, usePerc = nums
        if used == 0:
            blank = (x, y)
        if used > wallThreshold:
            walls.add((x, y))
    
    q = deque([(0, goal, blank)])
    v = set()
    lastStep = -1
    
    while len(q) > 0:
        step, goalPos, blankPos = q.popleft()
        
        state = (goalPos, blankPos)
        if state in v:
            continue
        v.add(state)
        
        if goalPos == (0, 0):
            print("ANS", step)
            return
        
        if step > lastStep:
            lastStep = step
            print("STEP", step, len(q))
        
        blankX, blankY = blankPos
        for xOffset, yOffset in CARDINAL_NEIGHBORS:
            nodeToMove = (blankX + xOffset, blankY + yOffset)
            if is_valid(nodeToMove):
                if nodeToMove == goalPos:
                    q.append((step + 1, blankPos, goalPos))
                else:
                    q.append((step + 1, goalPos, nodeToMove))
    print("FAIL")

if __name__ == "__main__":
    main()