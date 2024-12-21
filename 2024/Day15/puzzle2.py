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
    left_boxes = set()
    right_boxes = set()
    index = 0
    player_pos = None
    while True:
        line = lines[index]
        if not line:
            break
        y = index
        for j in range(len(line)):
            x = j * 2
            ch = line[j]
            if ch == '#':
                walls.add((x, y))
                walls.add((x + 1, y))
            elif ch == 'O':
                left_boxes.add((x, y))
                right_boxes.add((x + 1, y))
            elif ch == '@':
                player_pos = (x, y)
        index += 1
    width = len(lines[0]) * 2
    height = index
    index += 1
    assert player_pos is not None

    while index < len(lines):
        line = lines[index]
        for ch in line:
            move = arrow(ch)
            assert move is not None
            player_pos = process_move(move, player_pos, walls, left_boxes, right_boxes)
        index += 1

    # print_grid(width, height, player_pos, walls, left_boxes, right_boxes)
    total = 0
    for box in left_boxes:
        x, y = box
        coordinate = 100 * y + x
        total += coordinate
    print(total)

def print_grid(width, height, player_pos, walls, left_boxes, right_boxes):
    s = ""
    for y in range(height):
        for x in range(width):
            if (x, y) in walls:
                s += "#"
            elif (x, y) in left_boxes:
                s += "["
            elif (x, y) in right_boxes:
                s += "]"
            elif (x, y) == player_pos:
                s += "@"
            else:
                s += "."
        s += "\n"
    print(s)

def process_move(move, player_pos, walls, left_boxes, right_boxes):
    if can_move_recursive(move, player_pos, walls, left_boxes, right_boxes):
        return do_move(move, player_pos, left_boxes, right_boxes)
    return player_pos

def can_move_recursive(move, pos, walls, left_boxes, right_boxes):
    next_pos = addT(pos, move)
    if next_pos in walls:
        return False
    has_box_left = next_pos in left_boxes
    has_box_right = next_pos in right_boxes
    if not has_box_left and not has_box_right:
        return True
    assert not (has_box_left and has_box_right)
    if move == LEFT:
        return can_move_recursive(move, next_pos, walls, left_boxes, right_boxes)
    elif move == RIGHT:
        return can_move_recursive(move, next_pos, walls, left_boxes, right_boxes)
    else:
        if has_box_left:
            return can_move_recursive(move, next_pos, walls, left_boxes, right_boxes) and can_move_recursive(move, addT(next_pos, RIGHT), walls, left_boxes, right_boxes)
        if has_box_right:
            return can_move_recursive(move, next_pos, walls, left_boxes, right_boxes) and can_move_recursive(move, addT(next_pos, LEFT), walls, left_boxes, right_boxes)

# Assumes the move is valid
def do_move(move, player_pos, left_boxes, right_boxes):
    next_player_pos = addT(player_pos, move)
    left_boxes_to_add = set()
    right_boxes_to_add = set()
    q = deque()
    visited = set()
    q.append(next_player_pos)
    while len(q):
        pos = q.pop()
        if pos in visited:
            continue
        visited.add(pos)
        if pos in left_boxes:
            right_pos = addT(pos, RIGHT)
            assert right_pos in right_boxes
            left_boxes.remove(pos)
            right_boxes.remove(right_pos)
            left_boxes_to_add.add(addT(pos, move))
            right_boxes_to_add.add(addT(right_pos, move))
            q.append(addT(pos, move))
            q.append(addT(right_pos, move))
        elif pos in right_boxes:
            left_pos = addT(pos, LEFT)
            assert left_pos in left_boxes
            left_boxes.remove(left_pos)
            right_boxes.remove(pos)
            left_boxes_to_add.add(addT(left_pos, move))
            right_boxes_to_add.add(addT(pos, move))
            q.append(addT(left_pos, move))
            q.append(addT(pos, move))
    left_boxes.update(left_boxes_to_add)
    right_boxes.update(right_boxes_to_add)
    return next_player_pos

if __name__ == "__main__":
    main()