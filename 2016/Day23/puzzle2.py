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
    skips = [None for _ in instructions]
    i = 0
    addSkips = 0
    multSkips = 0
    ops = [instruction[0] for instruction in instructions]
    
    while i < len(instructions):
        if i < len(instructions) - 2 and ["inc", "dec", "jnz"] == ops[i:i+3]:
            a = instructions[i][1]
            b1 = instructions[i+1][1]
            b2 = instructions[i+2][1]
            v1 = instructions[i+2][2]
            unique = set([a, b1])
            if len(unique) == 2 and b1 == b2 and v1 == "-2":
                skips[i] = ("add", a, b1)
                addSkips += 1
        elif i < len(instructions) - 5 and ["cpy", "inc", "dec", "jnz", "dec", "jnz"] == ops[i:i+6]:
            a = instructions[i][1]
            b1 = instructions[i][2]
            c = instructions[i+1][1]
            b2 = instructions[i+2][1]
            b3 = instructions[i+3][1]
            v1 = instructions[i+3][2]
            d1 = instructions[i+4][1]
            d2 = instructions[i+5][1]
            v2 = instructions[i+5][2]
            unique = set([a, b1, c, d1])
            if len(unique) == 4 and b1 == b2 and b2 == b3 and d1 == d2 and v1 == "-2" and v2 == "-5":
                skips[i] = ("mult", c, a, d1)
                multSkips += 1
            else:
                print("Fake skip")
        
        i += 1
    #print(addSkips, "add skips found,", multSkips, "mult skips found")
    return skips
    
def main():
    pc = 0
    instructions = [words(line) for line in lines]
    skips = find_skips(instructions)
    while pc < len(instructions):
        w = instructions[pc]
        print(pc, w, registers)
        if w[0] == "cpy":
            if skips[pc] is not None and skips[pc][0] == "mult":
                op, target, a, b = skips[pc]
                print("MULT SKIP: " + target + " += " + a + " * " + b)
                registers[target] += resolve(a) * resolve(b)
                pc += 6
                continue
            xVal = resolve(w[1])
            y = w[2]
            if y in registers:
                registers[y] = xVal
        elif w[0] == "inc":
            if skips[pc] is not None and skips[pc][0] == "add":
                op, a, b = skips[pc]
                print("ADD SKIP: " + a + " += " + b)
                registers[a] += resolve(b)
                registers[b] = 0
                pc += 3
                continue
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
                print(pc + offset, instructions[pc+offset])
                skips = find_skips(instructions)
            print(registers)
        pc += 1
    print("ANS", registers["a"])

if __name__ == "__main__":
    main()