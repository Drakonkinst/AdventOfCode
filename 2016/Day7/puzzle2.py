import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    keep = 3
    for line in lines:
        prev = deque()
        i = 0
        hypernet = False
        hyper = set()
        notHyper = set()
        good = False
        while i < len(line):
            ch = line[i]

            if ch == "[":
                hypernet = True
                prev.clear()
            elif ch == "]":
                hypernet = False
                prev.clear()
            
            prev.append(ch)
            while len(prev) > keep:
                prev.popleft()
            if len(prev) == 3:
                if prev[0] == prev[2] and prev[0] != prev[1]:
                    A = prev[0]
                    B = prev[1]
                    ABA = A + B + A
                    BAB = B + A + B
                    if hypernet:
                        hyper.add(BAB)
                        if BAB in notHyper:
                            good = True
                            break
                    else:
                        notHyper.add(ABA)
                        if ABA in hyper:
                            good = True
                            break
            i += 1
        if good:
            total += 1
        
    print(total)

if __name__ == "__main__":
    main()