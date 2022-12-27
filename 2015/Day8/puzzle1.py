import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def is_hex(ch):
    return ch in HEX_STR

def main():
    a = 0
    b = 0
    for line in lines:
        a += len(line)
        i = 1
        x = 0
        while i < len(line) - 1:
            ch = line[i]
            if ch == '\\':
                charsRemaining = len(line) - i - 2
                if charsRemaining >= 1:
                    if charsRemaining >= 3 and line[i + 1] == 'x' and is_hex(line[i + 2]) and is_hex(line[i + 3]):
                        x += 1
                        i += 3
                    else:
                        x += 1
                        i += 1
                else:
                    assert False
            else:
                x += 1
            i += 1
        b += x
        #print(line, x, len(line))
    print(a - b)

if __name__ == "__main__":
    main()