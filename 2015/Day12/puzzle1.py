import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def count(x):
    if type(x) is int:
        return x
    if type(x) is dict:
        n = 0
        for k, v, in x.items():
            n += count(v)
        return n
    if type(x) is list:
        n = 0
        for v in x:
            n += count(v)
        return n
    return 0

def main():
    y = parseJSON(lines[0])
    total = 0
    print(count(y))
    
if __name__ == "__main__":
    main()