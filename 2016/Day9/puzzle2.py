import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    q = deque([(lines[0], 1)])
    total = 0
    while len(q) > 0:
        text, count = q.pop()
        i = 0
        while i < len(text):
            ch = text[i]
            if ch == "(":
                end = text.index(")", i)
                marker = ints(text[i + 1:end])
                length = marker[0]
                repeat = marker[1]
                q.append((text[end + 1:end + length + 1], count * repeat))
                #total += count * length * repeat
                i = end + length + 1
            else:
                total += count
                i += 1
    print(total)

if __name__ == "__main__":
    main()