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
    index = 0
    for i in range(0, len(lines), 4):
        ax, ay = ints(lines[i])
        bx, by = ints(lines[i + 1])
        gx, gy = ints(lines[i + 2])
        min_solution = find_min_solution(ax, ay, bx, by, gx, gy)
        if min_solution is not None:
            num_tokens_a, num_tokens_b, cost = min_solution
            total += cost
    print(total)

def find_min_solution(ax, ay, bx, by, gx, gy):
    min_a = -1
    min_b = -1
    min_tokens = sys.maxsize
    for a in range(101):
        b1 = (gx - a * ax) / bx
        b2 = (gy - a * ay) / by
        b = int(b1)
        if b1 == b and b1 == b2:
            # Valid solution, minimize cost
            tokens = COST_A * a + COST_B * b
            if tokens < min_tokens:
                min_tokens = tokens
                min_a = a
                min_b = b
    if min_a < 0:
        return None
    return min_a, min_b, min_tokens

if __name__ == "__main__":
    main()