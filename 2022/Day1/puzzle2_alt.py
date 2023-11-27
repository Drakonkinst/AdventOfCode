import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    top1 = TopN(3)
    currSum = 0
    for line in lines:
        if not line:
            top1.add(currSum)
            currSum = 0
        else:
            currSum += ints(line)[0]
    top1.add(currSum)
    print(sum(top1.data))

if __name__ == "__main__":
    main()