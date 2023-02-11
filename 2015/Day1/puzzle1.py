import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    n = 0
    for ch in lines[0]:
        if ch == '(':
            n += 1
        else:
            n -= 1
    print(n)

if __name__ == "__main__":
    main()