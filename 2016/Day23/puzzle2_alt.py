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
registers["a"] = 12

def resolve(x):
    if x in registers:
        return registers[x]
    return int(x)

def find_skips(instructions):
    ops = [instruction[0] for instruction in instructions]
    skips = [None for _ in instructions]
    i = 0
    while i < len(instructions) - 5:
        if ["cpy", "inc", "dec", "jnz", "dec", "jnz"] == ops[i:i+6]:
            skips[i] = ("mult", instructions[i+1][1], instructions[i][1], instructions[i+4][1])
        i += 1
    return skips

# Add skips without mult skips never actually happen, so we can simplify the logic
def main():
    pc = 0
    instructions = [words(line) for line in lines]
    skips = find_skips(instructions)
    while pc < len(instructions):
        w = instructions[pc]
        #print(pc, w, registers)
        if w[0] == "cpy":
            if skips[pc] is not None and skips[pc][0] == "mult":
                op, target, a, b = skips[pc]
                registers[target] += resolve(a) * resolve(b)
                pc += 6
                continue
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
            # Assume tgl is the only tgl instruction in the program
            if 0 <= pc + offset < len(instructions) and offset != 0:
                instruction = instructions[pc + offset]
                if instruction[0] == "inc":
                    instruction[0] = "dec"
                elif len(instruction) == 2:
                    instruction[0] = "inc"
                elif instruction[0] == "jnz":
                    instruction[0] = "cpy"
                elif len(instruction) == 3:
                    instruction[0] = "jnz"
                #print(pc + offset, instructions[pc+offset])
                skips = find_skips(instructions)
            #print(registers)
        pc += 1
    print("ANS", registers["a"])

if __name__ == "__main__":
    main()