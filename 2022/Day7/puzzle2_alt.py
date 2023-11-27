import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    dirEntries = {}
    dirSize = {}
    
    p = []
    i = 0
    while i < len(lines):
        w = words(lines[i])
        if w[1] == "cd":
            if w[2] == "/":
                p = [""]
            elif w[2] == "..":
                p.pop()
            else:
                p.append(w[2])
        elif w[1] == "ls":
            i += 1
            entries = []
            while i < len(lines) and lines[i][0] != "$":
                w2 = words(lines[i])
                if w2[0] == "dir":
                    # Format: (is_file=False, dir_name)
                    entries.append((False, w2[1]))
                else:
                    val = int(w2[0])
                    # Format: (is_file=True, name, size)
                    entries.append((True, w2[1], val))
                i += 1
            dirEntries["/".join(p)] = entries
            i -= 1
        i += 1
        
    q = deque()
    q.append("")
    while q:
        currPath = q.popleft()
        entries = dirEntries[currPath]
        size = 0
        cannotCompute = False
        for f in entries:
            if f[0]:
                size += f[2]
            else:
                fullPath = currPath + "/" + f[1]
                if fullPath in dirSize:
                    size += dirSize[fullPath]
                else:
                    q.append(fullPath)
                    cannotCompute = True
        if cannotCompute:
            q.append(currPath)
        else:
            dirSize[currPath] = size
    
    memRemaining = 70000000 - dirSize[""]
    memNeeded = 30000000 - memRemaining
    candidates = []
    for k in dirSize:
        if dirSize[k] >= memNeeded:
            candidates.append((dirSize[k], k))
    candidates.sort()
    print(candidates[0][0])

if __name__ == "__main__":
    main()