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
    
    t = lines[-1]
    s = set()
    for i in range(len(t)):
        ch = t[i]
        if ch in r:
            for rs in r[ch]:
                s.add(t[:i] + rs + t[i + 1:])
        if i < len(t) - 1:
            nextTwo = ch + t[i + 1]
            if nextTwo in r:
                for rs in r[nextTwo]:
                    s.add(t[:i] + rs + t[i + 2:])
    print(len(s))

if __name__ == "__main__":
    main()