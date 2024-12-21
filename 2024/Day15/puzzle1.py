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
    walls = set()
    boxes = set()
    index = 0
    player_pos = None
    while True:
        line = lines[index]
        if not line:
            break
        y = index
        for x in range(len(line)):
            ch = line[x]
            if ch == '#':
                walls.add((x, y))
            elif ch == 'O':
                boxes.add((x, y))
            elif ch == '@':
                player_pos = (x, y)
        index += 1
    index += 1
    assert player_pos is not None

    while index < len(lines):
        line = lines[index]
        for ch in line:
            move = arrow(ch)
            assert move is not None
            player_pos = process_move(move, player_pos, walls, boxes)
        index += 1

    total = 0
    for box in boxes:
        x, y = box
        coordinate = 100 * y + x
        total += coordinate
    print(total)

def process_move(move, player_pos, walls, boxes):
    if can_move(move, player_pos, walls, boxes):
        return do_move(move, player_pos, boxes)
    return player_pos

def can_move(move, player_pos, walls, boxes):
    next_pos = player_pos
    is_good = True
    while True:
        next_pos = addT(next_pos, move)
        if next_pos in walls:
            is_good = False
            break
        if next_pos not in boxes:
            break
    return is_good

def do_move(move, player_pos, boxes):
    next_player_pos = addT(player_pos, move)
    shifts_box = next_player_pos in boxes
    if shifts_box:
        boxes.remove(next_player_pos)
        next_free_space = next_player_pos
        while True:
            next_free_space = addT(next_free_space, move)
            if next_free_space not in boxes:
                break
        boxes.add(next_free_space)
    return next_player_pos

if __name__ == "__main__":
    main()