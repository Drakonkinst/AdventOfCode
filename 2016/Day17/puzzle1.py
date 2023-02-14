import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

open_chars = set(["b", "c", "d", "e", "f"])
width = 4
height = 4

def is_open(ch):
    return ch in open_chars

def is_valid(x, y):
    return 0 <= x < width and 0 <= y < height

def main():
    passcode = lines[0]

    q = deque([(0, 0, "")])
    v = set()
    while len(q) > 0:
        x, y, path = q.popleft()
        if (x, y, path) in v:
            v.add((x, y, path))
        hashValue = md5(passcode + path)

        if x == width - 1 and y == width - 1:
            print("ANS", path, len(path))
            return
        
        if is_valid(x, y - 1) and is_open(hashValue[0]):
            q.append((x, y - 1, path + "U"))
        if is_valid(x, y + 1) and is_open(hashValue[1]):
            q.append((x, y + 1, path + "D"))
        if is_valid(x - 1, y) and is_open(hashValue[2]):
            q.append((x - 1, y, path + "L"))
        if is_valid(x + 1, y) and is_open(hashValue[3]):
            q.append((x + 1, y, path + "R"))

if __name__ == "__main__":
    main()