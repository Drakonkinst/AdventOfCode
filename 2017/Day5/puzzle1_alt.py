import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    steps = 0
    arr = []
    for line in lines:
        arr.append(ints(line)[0])
    index = 0
    while 0 <= index < len(arr):
        nextIndex = index + arr[index]
        arr[index] += 1
        index = nextIndex
        steps += 1
    print(steps)

if __name__ == "__main__":
    main()