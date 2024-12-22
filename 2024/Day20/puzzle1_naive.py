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
    start_pos = None
    end_pos = None
    walls = set()
    height = len(lines)
    width = len(lines[0])
    for y in range(height):
        for x in range(width):
            ch = lines[y][x]
            if ch == 'S':
                start_pos = (x, y)
            elif ch == 'E':
                end_pos = (x, y)
            elif ch == '#':
                walls.add((x, y))
    assert start_pos is not None and end_pos is not None

    q = deque()
    cheats_found = {}
    best_time_without_cheats = None
    visited = set()
    q.append((0, start_pos, None, None, None)) # time, current pos, prev pos, cheat pos 1, cheat pos 2
    while len(q):
        print(len(q))
        time, pos, prev_pos, cheat_start, cheat_end = q.popleft()
        key = (pos, cheat_start, cheat_end)
        if key in visited:
            continue
        visited.add(key)

        if pos == end_pos:
            if cheat_start is not None:
                assert cheat_end is not None
                cheat_key = (cheat_start, cheat_end)
                # Second condition should never happen, but just in case
                if cheat_key not in cheats_found or cheats_found[cheat_key] > time:
                    cheats_found[cheat_key] = time
                continue
            else:
                # Solved without cheats!
                best_time_without_cheats = time
                break
        for offset in CARDINAL_NEIGHBORS:
            next_pos = addT(pos, offset)
            if not in_bounds(next_pos, height, width) or next_pos == prev_pos:
                continue
            if next_pos in walls:
                # Optimization: Skip the outer boundary
                x, y = next_pos
                if x == 0 or y == 0 or x == width - 1 or y == height - 1:
                    continue

                if cheat_start is None:
                    # Can cheat through this wall
                    q.append((time + 1, next_pos, pos, next_pos, cheat_end))
                else:
                    # Cannot cheat through this wall
                    continue
            else:
                if cheat_end is None and cheat_start is not None:
                    # Optimization: Skip cheats that are already found
                    cheat_key = (cheat_start, next_pos)
                    if cheat_key in cheats_found:
                        continue
                    # Mark the end of the cheat
                    q.append((time + 1, next_pos, pos, cheat_start, next_pos))
                else:
                    # Continue as normal
                    q.append((time + 1, next_pos, pos, cheat_start, cheat_end))

    # print(best_time_without_cheats, cheats_found)
    total = 0
    for cheat_key, time_to_complete in cheats_found.items():
        time_saved = best_time_without_cheats - time_to_complete
        if time_saved >= 2:
            total += 1
    print(total)

if __name__ == "__main__":
    main()