import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    for line in lines:
        equation = ints(line)
        answer = equation[0]
        operands = equation[1:]
        if is_valid(operands, answer):
            total += answer
    print(total)

def is_valid(operands, answer):
    q = deque()
    q.append(operands)
    while len(q):
        equation = q.pop()
        if len(equation) == 1:
            if equation[0] == answer:
                return True
            continue
        first_operand = equation[0]
        second_operand = equation[1]
        remainder = equation[2:]
        q.append([first_operand + second_operand] + remainder)
        q.append([first_operand * second_operand] + remainder)
        q.append([int(str(first_operand) + str(second_operand))] + remainder)
    return False

if __name__ == "__main__":
    main()