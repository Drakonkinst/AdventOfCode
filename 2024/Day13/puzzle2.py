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
OFFSET = 0
OFFSET = 10000000000000

def main():
    total = 0
    index = 0
    for i in range(0, len(lines), 4):
        ax, ay = ints(lines[i])
        bx, by = ints(lines[i + 1])
        gx, gy = ints(lines[i + 2])
        gx += OFFSET
        gy += OFFSET
        min_solution = find_min_solution(ax, ay, bx, by, gx, gy)
        if min_solution is not None:
            num_tokens_a, num_tokens_b, cost = min_solution
            total += cost
    print(total)

def get_cost(a, b):
    return COST_A * a + COST_B * b

def find_min_solution(ax, ay, bx, by, gx, gy):
    max_a = math.ceil(min(gx / ax, gy / ay))
    b_given_max_a = max(math.floor(min((gx - max_a * ax) / bx, (gy - max_a * ay) / by)), 0)
    max_b = math.ceil(min(gx / bx, gy / by))
    a_given_max_b = max(math.floor(min((gx - max_a * ax) / bx, (gy - max_a * ay) / by)), 0)
    q = PriorityQueue()
    visited = set()
    # print((max_a, b_given_max_a), (max_b, a_given_max_b))
    q.put((get_cost(max_a, b_given_max_a), max_a, b_given_max_a))
    q.put((get_cost(a_given_max_b, max_b), a_given_max_b, max_b))
    while q:
        cost, a, b = q.get()
        print(cost, a, b)
        key = (a, b)
        if key in visited:
            continue
        visited.add(key)
        x = ax * a + bx * b
        y = ay * a + by * b
        if x == gx and y == gy:
            return (a, b, cost)
        elif x > gx or y > gy:
            if a > 0:
                q.put((get_cost(a - 1, b), a - 1, b))
            if b > 0:
                q.put((get_cost(a, b - 1), a, b - 1))
        else:
            if a < max_a:
                q.put((get_cost(a + 1, b), a + 1, b))
            if b < max_b:
                q.put((get_cost(a, b + 1), a, b + 1))
    return None


if __name__ == "__main__":
    main()