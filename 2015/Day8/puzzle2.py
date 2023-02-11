import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    a = 0
    b = 0
    for line in lines:
        a += len(line)
        i = 0
        x = 0
        while i < len(line):
            ch = line[i]
            if ch == '\\' or ch == '"':
                x += 2
            else:
                x += 1
            i += 1
        #print(line, x, len(line))
        b += x + 2
    print(b - a)

if __name__ == "__main__":
    main()