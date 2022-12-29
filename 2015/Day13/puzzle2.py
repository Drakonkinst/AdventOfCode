import sys, os, re, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    s = set()
    h = {}
    for line in lines:
        w = words(line)
        a = w[0]
        gain = w[2] == "gain"
        amount = (1 if gain else -1) * int(w[3])
        b = w[-1][:-1]
        h[(a, b)] = amount

        s.add(a)
        s.add(b)
    s.add("Me")
    
    maxN = -sys.maxsize
    l = len(s)
    for perm in itt.permutations(s):
        n = 0
        for i in range(l):
            a = perm[i]
            b = perm[(i - 1 + l) % l]
            if (a, b) in h:
                n += h[(a, b)]
            c = perm[(i + 1) % l]
            if (a, c) in h:
                n += h[(a, c)]
        maxN = max(maxN, n)
    print(maxN)

if __name__ == "__main__":
    main()