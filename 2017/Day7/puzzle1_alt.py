import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    data = {}
    for line in lines:
        w = words(line)
        name = w[0]
        val = ints(w[1])
        if len(w) > 3:
            children = " ".join(w[3:]).split(", ")
            data[name] = (val, children)
        else:
            data[name] = (val, [])
    
    hasNoParent = set([k for k in data])
    for k in data:
        for c in data[k][1]:
            if c in hasNoParent:
                hasNoParent.remove(c)
    print(list(hasNoParent)[0])

if __name__ == "__main__":
    main()