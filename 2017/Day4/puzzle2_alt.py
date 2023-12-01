import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    for line in lines:
        s = set()
        good = True
        for w in words(line):
            charArray = list(w)
            charArray.sort()
            sortedWord = "".join(charArray)
            if sortedWord in s:
                good = False
                break
            s.add(sortedWord)
        if good:
            total += 1
    print(total)

if __name__ == "__main__":
    main()