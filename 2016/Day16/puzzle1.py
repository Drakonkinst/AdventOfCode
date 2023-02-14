import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

# New size is always 2 * len(a) + 1
def dragon(a):
    b = "".join(["1" if ch == "0" else "0" for ch in a[::-1]])
    return a + "0" + b
    
def calc_num_loops(sn, n):
    numLoops = 0
    while sn < n:
        sn = 2 * sn + 1
        numLoops += 1
    return numLoops

def main():
    s = lines[0]
    n = 272
    
    numLoops = calc_num_loops(len(s), n)
    for i in range(numLoops):
        s = dragon(s)
    s = s[:n]
    
    while True:
        i = 0
        checkSum = ""
        while i < len(s):
            a = s[i]
            b = s[i + 1]
            if a == b:
                checkSum += "1"
            else:
                checkSum += "0"
            i += 2
        s = checkSum
        if len(s) % 2 != 0:
            break
    print(s)
    

if __name__ == "__main__":
    main()