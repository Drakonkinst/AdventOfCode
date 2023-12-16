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
    
    seq = lines[0].split(",")
    for step in seq:
        total += parse_step(step)
    print(total)

if __name__ == "__main__":
    main()