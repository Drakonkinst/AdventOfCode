import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

key = "abcd"
registers = {}


def resolve(x):
    if x in registers:
        return registers[x]
    return int(x)
    
def main():
    i = 1
    while True:
        for k in key:
            registers[k] = 0
        registers["a"] = i

        count = 0
        pc = 0
        nextExpectedOutput = 0
        instructions = [words(line) for line in lines]
        good = True
        while good and pc < len(instructions):
            w = instructions[pc]
            #print(w)
            if w[0] == "cpy":
                xVal = resolve(w[1])
                y = w[2]
                if y in registers:
                    registers[y] = xVal
            elif w[0] == "inc":
                x = w[1]
                registers[x] += 1
            elif w[0] == "dec":
                x = w[1]
                registers[x] -= 1
            elif w[0] == "jnz":
                xVal = resolve(w[1])
                y = resolve(w[2])
                if xVal != 0:
                    pc += y
                    continue
            elif w[0] == "tgl":
                offset = resolve(w[1])
                if 0 <= pc + offset < len(instructions):
                    instruction = instructions[pc + offset]
                    if instruction[0] == "inc":
                        instruction[0] = "dec"
                    elif len(instruction) == 2:
                        instruction[0] = "inc"
                    elif instruction[0] == "jnz":
                        instruction[0] = "cpy"
                    elif len(instruction) == 3:
                        instruction[0] = "jnz"
            elif w[0] == "out":
                val = resolve(w[1])
                if val == nextExpectedOutput:
                    count += 1
                    nextExpectedOutput = 1 - nextExpectedOutput
                    
                    if count % 1000 == 0:
                        #print(i, "passed", count)
                        # If it passes 1000, it's good enough
                        # Likely fell into a pattern I'm too lazy to do
                        # the math to find
                        # And I'm not ready to solve the halting problem
                        print("ANS", i)
                        return
                else:
                    good = False
            pc += 1
        i += 1

if __name__ == "__main__":
    main()