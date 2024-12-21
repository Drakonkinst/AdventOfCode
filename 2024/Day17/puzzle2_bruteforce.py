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

def run_program(initial_a, program):
    registers = [initial_a, 0, 0]
    ic = 0
    output = []
    while ic < len(program):
        opcode = program[ic]
        operand = program[ic + 1]
        func = opcode_to_func[opcode]
        ic = func(registers, ic, operand, output)
        # Check that it still matches input, don't have to finish the program
        if opcode == 5:
            if len(output) > len(program) or output[len(output) - 1] != program[len(output) - 1]:
                return None
    return output

def main():
    program = ints(lines[4])
    output = None
    initial_a = 0

    # This will take a LONG time to finish
    while output != program:
        initial_a += 1
        output = run_program(initial_a, program)
        if initial_a % 1000000 == 0:
            print("LOOP", initial_a)
    print(initial_a)

if __name__ == "__main__":
    main()