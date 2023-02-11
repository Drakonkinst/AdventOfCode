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
        if w[0] not in r:
            r[w[0]] = []
        r[w[0]].append(w[-1])
    
    g = lines[-1]
    
    s = set(["e"])
    q = deque([("e", 0)])
    lastStep = -1
    while len(q):
        t, step = q.popleft()
        if step > lastStep:
            lastStep = step
            print(step, len(q), t)
        if t == g:
            print("ANS", step)
            return
        for i in range(len(t)):
            ch = t[i]
            if ch in r:
                for rs in r[ch]:
                    nextStr = t[:i] + rs + t[i + 1:]
                    if nextStr not in s:
                        s.add(nextStr)
                        q.append((nextStr, step + 1))
            if i < len(t) - 1:
                nextTwo = ch + t[i + 1]
                if nextTwo in r:
                    for rs in r[nextTwo]:
                        nextStr = t[:i] + rs + t[i + 2:]
                        if nextStr not in s:
                            s.add(nextStr)
                            q.append((nextStr, step + 1))
    print(len(s))

if __name__ == "__main__":
    main()