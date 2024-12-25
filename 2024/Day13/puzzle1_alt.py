import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

COST_A = 3
COST_B = 1

def main():
    total = 0
    for i in range(0, len(lines), 4):
        ax, ay = ints(lines[i])
        bx, by = ints(lines[i + 1])
        gx, gy = ints(lines[i + 2])
        solution = find_solution(ax, ay, bx, by, gx, gy)
        if solution is not None:
            solution_a, solution_b = solution
            cost = get_cost(solution_a, solution_b)
            total += cost
    print(total)

def get_cost(a, b):
    return COST_A * a + COST_B * b

def find_solution(ax, ay, bx, by, gx, gy):
    # Algebra go brrrrr
    b = (ay * gx - ax * gy) / (ay * bx - ax * by)
    if int(b) != b:
        return None
    # Just to make sure
    a1 = (gx - b * bx) / ax
    a2 = (gy - b * by) / ay
    assert a1 == a2
    return int(a1), int(b)

if __name__ == "__main__":
    main()