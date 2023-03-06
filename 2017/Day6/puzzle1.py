import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def getMaxIndex(blocks):
    maxIndex = 0
    index = 1
    while index < len(blocks):
        if blocks[index] > blocks[maxIndex]:
            maxIndex = index
        index += 1
    return maxIndex

def main():
    blocks = ints(lines[0])
    alreadySeen = set()
    step = 0
    
    while True:
        step += 1
        maxIndex = getMaxIndex(blocks)
        maxValue = blocks[maxIndex]
        blocks[maxIndex] = 0
        incrementAll = maxValue // len(blocks)
        extra = maxValue % len(blocks)
        
        for i in range(len(blocks)):
            blocks[i] += incrementAll
        
        extraIndex = maxIndex
        for i in range(extra):
            extraIndex = (extraIndex + 1) % len(blocks)
            blocks[extraIndex] += 1
        
        state = tuple(blocks)
        if state in alreadySeen:
            break
        alreadySeen.add(state)
        
    print(step)

if __name__ == "__main__":
    main()