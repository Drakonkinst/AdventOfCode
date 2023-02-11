import sys, os, re, math, hashlib, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    p = lines[0]
    
    n = 8
    i = 0
    a = ""
    for j in range(n):
        while True:
            s = p + str(i)
            i += 1
            h = hashlib.md5(s.encode()).hexdigest()
            if h.startswith("00000"):
                a += h[5]
                print(a)
                break
    print(a)
        
if __name__ == "__main__":
    main()