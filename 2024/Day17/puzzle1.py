import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

A = 0
B = 1
C = 2
DEFAULT_IC_INCREMENT = 2

def literal_to_combo(registers, operand):
    if operand <= 3:
        return operand
    return registers[operand - 4]

def adv(registers, ic, operand, output):
    numerator = registers[A]
    denominator = 2 ** literal_to_combo(registers, operand)
    registers[A] = numerator // denominator
    return ic + DEFAULT_IC_INCREMENT

def bxl(registers, ic, operand, output):
    registers[B] = registers[B] ^ operand
    return ic + DEFAULT_IC_INCREMENT

def bst(registers, ic, operand, output):
    combo = literal_to_combo(registers, operand)
    registers[B] = combo % 8
    return ic + DEFAULT_IC_INCREMENT

def jnz(registers, ic, operand, output):
    if registers[A] != 0:
        return operand
    return ic + DEFAULT_IC_INCREMENT

def bxc(registers, ic, operand, output):
    registers[B] = registers[B] ^ registers[C]
    return ic + DEFAULT_IC_INCREMENT

def out(registers, ic, operand, output):
    combo = literal_to_combo(registers, operand)
    output.append(combo % 8)
    return ic + DEFAULT_IC_INCREMENT

def bdv(registers, ic, operand, output):
    numerator = registers[A]
    denominator = 2 ** literal_to_combo(registers, operand)
    registers[B] = numerator // denominator
    return ic + DEFAULT_IC_INCREMENT

def cdv(registers, ic, operand, output):
    numerator = registers[A]
    denominator = 2 ** literal_to_combo(registers, operand)
    registers[C] = numerator // denominator
    return ic + DEFAULT_IC_INCREMENT

opcode_to_func = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

def main():
    registers = [0, 0, 0]
    registers[A] = ints(lines[A])[0]
    registers[B] = ints(lines[B])[0]
    registers[C] = ints(lines[C])[0]
    program = ints(lines[4])

    ic = 0
    output = []
    while ic < len(program):
        opcode = program[ic]
        operand = program[ic + 1]
        func = opcode_to_func[opcode]
        ic = func(registers, ic, operand, output)
        # print(opcode, operand, ic, registers, output)
    print(",".join([str(i) for i in output]))

if __name__ == "__main__":
    main()