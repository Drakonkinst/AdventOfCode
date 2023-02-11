import sys, os, re, math, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    tris = []
    i = 0
    while i < len(lines):
        a = ints(lines[i])
        b = ints(lines[i + 1])
        c = ints(lines[i + 2])
        tris.append([a[0], b[0], c[0]])
        tris.append([a[1], b[1], c[1]])
        tris.append([a[2], b[2], c[2]])
        i += 3
    
    t = 0
    for tri in tris:
        m = max(tri)
        tri.remove(m)
        if tri[0] + tri[1] > m:
            t += 1
    print(t)

if __name__ == "__main__":
    main()