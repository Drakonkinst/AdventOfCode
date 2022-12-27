import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    n = 0
    for line in lines:
        a = False
        b = False
        pairs = {}
        for i in range(len(line)):
            ch = line[i]
            if i >= 1:
                lastTwo = line[i - 1] + ch
                if lastTwo in pairs and pairs[lastTwo] < i - 1:
                    a = True
                pairs[lastTwo] = i
            if i >= 2:
                if line[i - 2] == line[i]:
                    b = True
        if a and b:
            n += 1
    print(n)

if __name__ == "__main__":
    main()