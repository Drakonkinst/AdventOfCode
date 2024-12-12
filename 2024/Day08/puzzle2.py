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
    nodes = {}
    num_rows = len(lines)
    num_cols = len(lines[0])
    # Read data
    for row in range(num_rows):
        for col in range(num_cols):
            ch = lines[row][col]
            if ch == '.':
                continue
            if ch not in nodes:
                nodes[ch] = []
            nodes[ch].append((row, col))

    # Find antinodes
    antinodes = set()
    for node_positions in nodes.values():
        if len(node_positions) < 2:
            # Will never have antinodes
            continue
        for node1, node2 in itt.combinations(node_positions, 2):
            offset = subT(node2, node1)
            # Loop past the second antinode
            antinode = node2
            while in_bounds(antinode, num_rows, num_cols):
                antinodes.add(antinode)
                antinode = addT(antinode, offset)
            # Loop before the first antinode
            antinode = node1
            while in_bounds(antinode, num_rows, num_cols):
                antinodes.add(antinode)
                antinode = subT(antinode, offset)
    # print_grid(num_rows, num_cols, nodes, antinodes)
    print(len(antinodes))

def print_grid(num_rows, num_cols, nodes, antinodes):
    for row in range(num_rows):
        s = ""
        for col in range(num_cols):
            s += get_char(row, col, nodes, antinodes)
        print(s)

def get_char(row, col, nodes, antinodes):
    for key, node_positions in nodes.items():
        if (row, col) in node_positions:
            return key
    if (row, col) in antinodes:
        return '#'
    return '.'

if __name__ == "__main__":
    main()