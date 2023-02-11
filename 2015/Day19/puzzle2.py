import sys, os, re, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    r = {}
    for line in lines:
        if len(line) == 0:
            break
        w = words(line)
        if w[-1] not in r:
            r[w[-1]] = []
        r[w[-1]].append(w[0])
    
    start = lines[-1]
    g = "e"
    
    s = set([start])
    q = deque([(start, 0)])
    minLen = len(start)
    lastStep = -1
    c = 0
    while len(q):
        t, step = q.pop()
        if t == g:
            print("ANS", step)
            return
        for i in range(len(t)):
            ch = t[i]
            for k, v in r.items():
                j = i
                good = True
                for l in range(len(k)):
                    if j >= len(t):
                        good = False
                        break
                    if k[l] != t[j]:
                        good = False
                        break
                    j += 1
                if good:
                    pre = t[:i]
                    post = t[i + len(k):]
                    for rs in v:
                        nextStr = pre + rs + post
                        if nextStr not in s:
                            s.add(nextStr)
                            q.append((nextStr, step + 1))
    assert False

if __name__ == "__main__":
    main()