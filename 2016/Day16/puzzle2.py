import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

# New size is always 2 * len(a) + 1
def dragon(a):
    b = ["1" if ch == "0" else "0" for ch in a[::-1]]
    return a + ["0"] + b
    
def calc_num_loops(sn, n):
    numLoops = 0
    while sn < n:
        sn = 2 * sn + 1
        numLoops += 1
    return numLoops

def main():
    s = [ch for ch in lines[0]]
    n = 35651584
    
    numLoops = calc_num_loops(len(s), n)
    print("numLoops", numLoops)
    for i in range(numLoops):
        s = dragon(s)
    s = s[:n]
    print("Generated")
    
    checkSum = [ch for ch in s]
    while True:
        i = 0
        nextCheckSum = ["0" for _ in range(len(checkSum) // 2)]
        while i < len(checkSum):
            a = checkSum[i]
            b = checkSum[i + 1]
            if a == b:
                nextCheckSum[i // 2] = "1"
            i += 2
        checkSum = nextCheckSum
        print(len(checkSum))
        if len(checkSum) % 2 != 0:
            s = "".join(checkSum)
            break
    print(s)
    

if __name__ == "__main__":
    main()