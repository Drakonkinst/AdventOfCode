import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

COST_STEP = 1
COST_TURN = 1000
def main():
    walls = set()
    start_pos = None
    end_pos = None
    prev_tiles = {}
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            ch = line[x]
            if ch == '#':
                walls.add((x, y))
            else:
                for offset in CARDINAL_NEIGHBORS:
                    prev_tiles[((x, y), offset)] = (sys.maxsize, [])
                if ch == 'S':
                    start_pos = (x, y)
                elif ch == 'E':
                    end_pos = (x, y)
    assert start_pos is not None and end_pos is not None

    q = PriorityQueue()
    q.put((0, start_pos, RIGHT, None, None))
    visited = set()
    best_cost = None
    end_nodes = set()
    num_unique_paths = 0
    while q:
        cost, pos, direction, prev_pos, prev_direction = q.get()
        key = (pos, direction, prev_pos, prev_direction)
        if best_cost is not None and cost > best_cost:
            break
        if pos == end_pos:
            end_nodes.add((pos, direction))
            num_unique_paths += 1
            best_cost = cost
        if key in visited:
            continue
        visited.add(key)
        ahead_pos = addT(pos, direction)
        if ahead_pos not in walls:
            add_prev_tile(cost + COST_STEP, ahead_pos, direction, pos, direction, q, prev_tiles)
        current_direction_index = CARDINAL_NEIGHBORS.index(direction)
        counterclockwise = CARDINAL_NEIGHBORS[(current_direction_index - 1 + len(CARDINAL_NEIGHBORS)) % len(CARDINAL_NEIGHBORS)]
        clockwise = CARDINAL_NEIGHBORS[(current_direction_index + 1) % len(CARDINAL_NEIGHBORS)]
        add_prev_tile(cost + COST_TURN, pos, counterclockwise, pos, direction, q, prev_tiles)
        add_prev_tile(cost + COST_TURN, pos, clockwise, pos, direction, q, prev_tiles)

    best_path = set()
    visited = set()
    q = deque()

    # print(num_unique_paths, best_cost, end_nodes)

    # for k, v in prev_tiles.items():
    #     print(k, "->", v)

    for end_node in end_nodes:
        q.append((best_cost, end_node))

    while len(q):
        key = q.pop()
        cost, node = key
        if node in visited:
            continue
        # print("Examining", node, "with cost", cost)
        visited.add(node)
        pos, direction = node
        best_path.add(pos)
        if pos == start_pos:
            continue
        prev_cost, prevs = prev_tiles[node]
        # print("Found", len(prevs), "paths with cost", prev_cost)
        assert prev_cost <= cost
        for prev in prevs:
            q.append((prev_cost, prev))

    # print_grid(lines, walls, best_path)
    print(len(best_path))

def print_grid(lines, walls, best_path):
    s = ""
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (x, y) in walls:
                s += "#"
            elif (x, y) in best_path:
                s += "O"
            else:
                s += "."
        s += "\n"
    print(s)

def add_prev_tile(cost, next_pos, next_direction, prev_pos, prev_direction, q, prev_tiles):
    prev_key = (prev_pos, prev_direction)
    next_key = (next_pos, next_direction)
    old_cost = prev_tiles[next_key][0]
    if cost > old_cost:
        # Ignore paths that are definitely worse
        return
    if cost < old_cost:
        # If it's a better path, forget about the old ones
        prev_tiles[next_key] = (cost, [])
    prev_tiles[next_key][1].append(prev_key)
    q.put((cost, next_pos, next_direction, prev_pos, prev_direction))


if __name__ == "__main__":
    main()