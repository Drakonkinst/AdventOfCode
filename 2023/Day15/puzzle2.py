import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def parse_step(step):
    val = 0
    for ch in step:
        asciiVal = ord(ch)
        val += asciiVal
        val *= 17
        val = val % 256
    return val

def main():
    total = 0
    boxes = [[] for _ in range(256)]
    seq = lines[0].split(",")
    for step in seq:
        hasEqual = "=" in step
        if hasEqual:
            label = step[:step.index("=")]
        else:
            label = step[:-1]
        boxNum = parse_step(label)
        
        box = boxes[boxNum]
        if hasEqual:
            focalLength = int(step[step.index("=")+1:])
            found = False
            for i in range(len(box)):
                (key, val) = box[i]
                if key == label:
                    box[i] = (key, focalLength)
                    found = True
                    break
            if not found:
                box.append((label, focalLength))
        else:
            for i in range(len(box)-1, -1, -1):
                (key, val) = box[i]
                if key == label:
                    del box[i]
                    break

    for i in range(len(boxes)):
        boxNum = i + 1
        box = boxes[i]
        for j in range(len(box)):
            lensNum = j + 1
            (key, val) = box[j]
            total += boxNum * lensNum * val
    print(total)

if __name__ == "__main__":
    main()