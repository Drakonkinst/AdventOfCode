import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def parse_instruction(s):
    w = words(s)
    if s.startswith("swap position"):
        X = int(w[2])
        Y = int(w[-1])
        return ("swap_pos", [X, Y])
    elif s.startswith("swap letter"):
        X = w[2]
        Y = w[-1]
        return ("swap_letter", [X, Y])
    elif s.startswith("rotate left"):
        X = int(w[2])
        return ("rotate", [-X])
    elif s.startswith("rotate right"):
        X = int(w[2])
        return ("rotate", [X])
    elif s.startswith("rotate based"):
        X = w[-1]
        return ("rotate_based", [X])
    elif s.startswith("reverse positions"):
        X = int(w[2])
        Y = int(w[-1])
        return ("reverse", [X, Y])
    elif s.startswith("move position"):
        X = int(w[2])
        Y = int(w[-1])
        return ("move", [X, Y])
    else:
        assert False

def rotate(s, shift):
    splitIndex = (len(s) - shift + (abs(shift) * len(s))) % len(s)
    a = s[:splitIndex]
    b = s[splitIndex:]
    return b + a

def reverse(s, start, end):
    toReverse = s[start:end+1]
    before = s[:start]
    after = s[end+1:]
    toReverse.reverse()
    return before + toReverse + after

def process_instruction(s, instruction):
    op, args = instruction
    X = args[0]
    Y = args[1] if len(args) >= 2 else None
    
    if op == "swap_pos":
        s[X], s[Y] = s[Y], s[X]
    elif op == "swap_letter":
        for i in range(len(s)):
            ch = s[i]
            if ch == X:
                s[i] = Y
            elif ch == Y:
                s[i] = X
    elif op == "rotate":
        s = rotate(s, X)
    elif op == "rotate_based":
        index = s.index(X)
        bonus = 1
        if index >= 4:
            bonus += 1
        s = rotate(s, index + bonus)
    elif op == "reverse":
        s = reverse(s, X, Y)
    elif op == "move":
        ch = s.pop(X)
        s.insert(Y, ch)
    else:
        assert False
    return s

def main():
    start = "abcdefgh"
    # Represent string as array so it is mutable
    s = [ch for ch in start]
    instructions = []
    for line in lines:
        instructions.append(parse_instruction(line))
    for instruction in instructions:
        s = process_instruction(s, instruction)
    # Convert back to string
    result = "".join(s)
    print(result)

if __name__ == "__main__":
    main()