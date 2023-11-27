import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    top1 = TopN(1)
    currSum = 0
    for line in lines:
        if not line:
            top1.add(currSum)
            currSum = 0
        else:
            currSum += ints(line)[0]
    top1.add(currSum)
    print(top1.data[0])

if __name__ == "__main__":
    main()