import sys, os, re, math, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    # Read package weights
    l = []
    for line in lines:
        l.append(int(line))
    #print(l)
    
    # Now we know the target sum of each of the 3 groups
    s = sum(l) // 3
    
    # Find smallest combination that creates s
    sn = 1
    cn = []
    while True:
        for c in itt.combinations(l, sn):
            if sum(c) == s:
                cn.append(c)
        if len(cn) > 0:
            break
        sn += 1
    
    # Configuration of the other two doesn't matter
    #print(sn, cn)
    
    mc = cn[0]
    mp = math.prod(mc)
    for c in cn:
        if math.prod(c) < mp:
            mc = c
            mp = math.prod(mc)
    
    print(mp, mc)


if __name__ == "__main__":
    main()