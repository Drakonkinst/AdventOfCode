import sys, os, re, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    reg = [1, 0]

    l = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        w = words(line)
        if w[0] == "hlf":
            ri = LOWERCASE_STR.index(w[1])
            reg[ri] //= 2
        elif w[0] == "tpl":
            ri = LOWERCASE_STR.index(w[1])
            reg[ri] *= 3
        elif w[0] == "inc":
            ri = LOWERCASE_STR.index(w[1])
            reg[ri] += 1
        elif w[0] == "jmp":
            j = ints(w[1])[0]
            i += j
            continue
        elif w[0] == "jie":
            j = ints(w[2])[0]
            ri = LOWERCASE_STR.index(w[1][:-1])
            if reg[ri] % 2 == 0:
                i += j
                continue
        elif w[0] == "jio":
            j = ints(w[2])[0]
            ri = LOWERCASE_STR.index(w[1][:-1])
            if reg[ri] == 1:
                i += j
                continue
        i += 1
    print(reg)

if __name__ == "__main__":
    main()