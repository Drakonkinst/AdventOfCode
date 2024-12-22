import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

# This one doesn't work, and kept returning answers that were too high
# I think because 1) I wasn't considering that ambiguities need to be explored
# and 2) wasn't considering which situations were ambiguities properly.
#
# It's only not an ambiguity if going in one axis will end up stepping on an
# invalid tile
file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    for code in lines:
        sequence_length = get_sequence_length(code)
        numeric_part = get_numeric_part(code)
        complexity = sequence_length * numeric_part
        # print(sequence_length, "*", numeric_part, "=", complexity)
        total += complexity
    print(total)

# We can assume that the code is always a number with an A at the end
def get_numeric_part(code):
    return int(code[:-1])

def get_sequence_length(code):
    # At the end of each character in the code, all directional keypads must end
    # up at A
    print(code)
    possible_numeric_sequences = get_numeric_sequences(code)
    min_sequence_length = sys.maxsize
    for numeric_sequence in possible_numeric_sequences:
        # print(numeric_sequence)
        directional_sequence_1 = get_directional_sequence(numeric_sequence)
        # print(directional_sequence_1)
        directional_sequence_2 = get_directional_sequence(directional_sequence_1)
        # print(directional_sequence_2)
        if len(directional_sequence_2) < min_sequence_length:
            min_sequence_length = len(directional_sequence_2)
    return min_sequence_length

numeric_keypad_coords = {
    'A': (2, 3),
    '0': (1, 3),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0)
}

def get_numeric_sequences(code):
    initial_pos = numeric_keypad_coords['A']
    sequences = []
    # The numeric keypad has ambiguous sequences which the directional keypad does not
    # Explore all possibilities
    q = deque()
    q.append((code, initial_pos, ""))
    while len(q):
        remaining_code, pos, sequence_so_far = q.pop()
        if len(remaining_code) <= 0:
            sequences.append(sequence_so_far)
            continue
        # The shortest path will always be moving first on one axis, then the other
        # There are point of ambiguity where either could work
        definitely_vertical_first = pos[1] == 3
        definitely_horizontal_first = pos[0] == 0
        ambiguous = not definitely_vertical_first and not definitely_horizontal_first
        next_ch = remaining_code[0]
        next_pos = numeric_keypad_coords[next_ch]

        if definitely_vertical_first or ambiguous:
            vertical_sequence = sequence_so_far
            vertical_sequence += add_vertical(next_pos, pos)
            vertical_sequence += add_horizontal(next_pos, pos)
            vertical_sequence += "A"
            q.append((remaining_code[1:], next_pos, vertical_sequence))

        if definitely_horizontal_first or ambiguous:
            horizontal_sequence = sequence_so_far
            horizontal_sequence += add_horizontal(next_pos, pos)
            horizontal_sequence += add_vertical(next_pos, pos)
            horizontal_sequence += "A"
            q.append((remaining_code[1:], next_pos, horizontal_sequence))

    return sequences

def add_vertical(next_pos, pos):
    sequence = ""
    while next_pos[1] != pos[1]:
        if next_pos[1] < pos[1]:
            sequence += "^"
            pos = addT(pos, UP)
        else:
            sequence += "v"
            pos = addT(pos, DOWN)
    return sequence

def add_horizontal(next_pos, pos):
    sequence = ""
    while next_pos[0] != pos[0]:
        if next_pos[0] < pos[0]:
            sequence += "<"
            pos = addT(pos, LEFT)
        else:
            sequence += ">"
            pos = addT(pos, RIGHT)
    return sequence

directional_keypad_coords = {
    'A': (2, 0),
    '^': (1, 0),
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1),
}

def get_directional_sequence(code):
    pos = directional_keypad_coords['A']
    sequence = ""
    for ch in code:
        next_pos = directional_keypad_coords[ch]
        # The shortest path will always be moving first on one axis, then the other
        go_vertical_first = True
        # If on the leftmost fringe, go horizontal first
        if pos[0] == 0:
            go_vertical_first = False

        if go_vertical_first:
            sequence += add_vertical(next_pos, pos)
            sequence += add_horizontal(next_pos, pos)
        else:
            sequence += add_horizontal(next_pos, pos)
            sequence += add_vertical(next_pos, pos)
        sequence += "A"
        pos = next_pos
    return sequence

if __name__ == "__main__":
    main()