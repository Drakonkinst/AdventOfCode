import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    text = lines[0]
    total = 0
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "(":
            end = text.index(")", i)
            marker = ints(text[i + 1:end])
            length = marker[0]
            repeat = marker[1]
            total += length * repeat
            i = end + length + 1
        else:
            total += 1
            i += 1
    print(total)

if __name__ == "__main__":
    main()