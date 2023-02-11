import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

def main():
    curr = "3113322113"
    n = 50
    for i in range(n):
        next = ""
        lastCh = ""
        count = 0
        for ch in curr:
            if ch == lastCh:
                count += 1
            elif count == 0:
                lastCh = ch
                count = 1
            else:
                next += str(count) + lastCh
                lastCh = ch
                count = 1
        next += str(count) + lastCh
        curr = next
    print(len(curr))

if __name__ == "__main__":
    main()