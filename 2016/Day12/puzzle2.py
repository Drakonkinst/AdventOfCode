import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

key = "abcd"
registers = {}
for k in key:
    registers[k] = 0
registers["c"] = 1

def resolve(x):
    if x in registers:
        return registers[x]
    return int(x)
    
def main():
    pc = 0
    while pc < len(lines):
        w = words(lines[pc])
        if w[0] == "cpy":
            xVal = resolve(w[1])
            y = w[2]
            registers[y] = xVal
        elif w[0] == "inc":
            x = w[1]
            registers[x] += 1
        elif w[0] == "dec":
            x = w[1]
            registers[x] -= 1
        elif w[0] == "jnz":
            xVal = resolve(w[1])
            y = int(w[2])
            if xVal != 0:
                pc += y
                continue
        pc += 1
    print(registers["a"])

if __name__ == "__main__":
    main()