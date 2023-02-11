import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    adj = {}
    v = set()
    for line in lines:
        w = words(line)
        f = w[0]
        t = w[2]
        v.add(f)
        v.add(t)
        c = int(w[-1])
        
        if f not in adj:
            adj[f] = []
        if t not in adj:
            adj[t] = []
        adj[f].append((t, c))
        adj[t].append((f, c))
    
    # Assume there are no cycles
    maxPathCost = -sys.maxsize
    maxPath = []
    q = deque()
    for s in adj.keys():
        q.append((s, 0, set(), [s]))
    while len(q) > 0:
        curr, pathCost, leftToVisit, path = q.pop()
        leftToVisit.add(curr)
        if len(leftToVisit) == len(adj):
            if pathCost > maxPathCost:
                maxPathCost = pathCost
                maxPath = path
            continue
        for i in adj[curr]:
            if i[0] not in leftToVisit:
                arr = path.copy()
                arr.append(i[0])
                q.append((i[0], pathCost + i[1], set(leftToVisit), arr))
    print(maxPathCost, " -> ".join(maxPath))

if __name__ == "__main__":
    main()