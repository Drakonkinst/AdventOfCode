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
    root = list(hasNoParent)[0]
    
    weightSums = {}
    q = deque()
    q.append(root)
    
    while q:
        name = q.popleft()
        weightSum = data[name][0]
        missing = []
        for c in data[name][1]:
            if c in weightSums:
                weightSum += weightSums[c]
            else:
                missing.append(c)
        if missing:
            q.extend(missing)
            q.append(name)
        else:
            weightSums[name] = weightSum
    
    # TODO: Now that we know the weights of everything, find the one that's imbalanced
if __name__ == "__main__":
    main()