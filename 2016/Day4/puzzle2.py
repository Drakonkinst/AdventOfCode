import sys, os, re, math, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    for line in lines:
        i = line.index("[")
        i2 = line.rindex("-")
        a = line[:i2]
        b = int(line[i2+1:i])
        c = line[i + 1:-1]
        
        f = {}
        for ch in a:
            if ch == "-":
                continue
            if ch in f:
                f[ch] += 1
            else:
                f[ch] = 1
        top5 = sorted(f.items(), key = lambda x: x[1] * 9999 - LOWERCASE_STR.index(x[0]), reverse=True)[:5]
        checksum = "".join([k[0] for k in top5])
        if checksum != c:
            continue
        
        name = ""
        for ch in a:
            if ch == "-":
                name += " "
                continue
            j = (LOWERCASE_STR.index(ch) + b) % len(LOWERCASE_STR)
            name += LOWERCASE_STR[j]
        if "north" in name:
            print(name, b)

if __name__ == "__main__":
    main()