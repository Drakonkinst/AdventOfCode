import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
import hashlib

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    n = 282749
    line = lines[0]
    while True:
        s = line + str(n)
        h = hashlib.md5(s.encode()).hexdigest()
        if h.startswith("000000"):
            print(n)
            return
        n += 1

if __name__ == "__main__":
    main()