import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    for line in lines:
        w = words(line)
        separatorIndex = w.index("|")
        winningNums = lmap(int, w[2:separatorIndex])
        myNums = lmap(int, w[separatorIndex + 1:])
        
        numWins = 0
        for myNum in myNums:
            if myNum in winningNums:
                numWins += 1
        if numWins > 0:
            total += 2 ** (numWins - 1)
    print(total)

if __name__ == "__main__":
    main()