import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    moves = lines[0]
    
    santaPos = (0, 0)
    robotPos = (0, 0)
    v = set([santaPos, robotPos])
    turn = True
    for ch in moves:
        offset = arrow(ch)
        
        # Move Santa or Robo-Santa depending on turn
        if turn:
            santaPos = addT(santaPos, offset)
            v.add(santaPos)
        else:
            robotPos = addT(robotPos, offset)
            v.add(robotPos)
        turn = not turn
        
    # Presents delivered is equal to number of unique houses visited
    print(len(v))

if __name__ == "__main__":
    main()