import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    keep = 4
    for line in lines:
        prev = deque()
        i = 0
        hypernet = False
        good = False
        bad = False
        while i < len(line):
            ch = line[i]

            if ch == "[":
                hypernet = True
                prev.clear()
            elif ch == "]":
                hypernet = False
                prev.clear()
            
            prev.append(ch)
            while len(prev) > keep:
                prev.popleft()
            if len(prev) == 4:
                if prev[0] == prev[3] and prev[1] == prev[2] and prev[0] != prev[1]:
                    if hypernet:
                        bad = True
                        break
                    else:
                        good = True
            i += 1
        if good and not bad:
            total += 1
        
    print(total)

if __name__ == "__main__":
    main()