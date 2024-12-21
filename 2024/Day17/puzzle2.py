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
        # Optimization: Stop trying once the output gets too long
        if len(output) > len(program):
            break
    return output

def matches_end(partial_output, expected_output):
    expected = expected_output[len(expected_output) - len(partial_output):]
    return partial_output == expected

def to_int(input_str):
    if input_str:
        return int(input_str, 8)
    return -1

BASE_8_DIGITS = "01234567"

def main():
    # The program always loops back to the beginning at the end, as long as A is not 0
    # By the structure of the program in the input, we know that it is composable
    # so we can pick potential digits that match the end of the program and work from there
    # We can assume that given the same length of initial_a, there will never be two values
    # that are both the solution -- the "lowest positive number" is largely a red herring
    # since length of the initial_a in base 8 must equal the output
    # The digits must be composed from base 8
    program = ints(lines[4])

    q = deque()
    q.append("")
    visited = set()
    while len(q):
        input_str = q.popleft()
        initial_a = to_int(input_str)
        if initial_a in visited:
            continue
        visited.add(initial_a)
        if initial_a >= 0:
            output = run_program(initial_a, program)
        else:
            output = []
        # print("Considering", input_str, initial_a, "->", output)
        if program == output:
            print(initial_a)
            return
        if not matches_end(output, program):
            continue
        for digit in BASE_8_DIGITS:
            q.append(input_str + digit)
    assert False

if __name__ == "__main__":
    main()