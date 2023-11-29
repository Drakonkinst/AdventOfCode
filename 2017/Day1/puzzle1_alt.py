import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    for line in lines:
        total = 0
        n = len(line)
        for i in range(len(line)):
            c = int(line[i])
            o = int(line[(i + 1) % n])
            if c == o:
                total += int(c)
        print(total)

if __name__ == "__main__":
    main()