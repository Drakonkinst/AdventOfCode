import sys, os, re, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    l = 0
    for line in lines:
        l += 1
    print(l)

if __name__ == "__main__":
    main()