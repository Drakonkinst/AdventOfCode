import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

# Feels disgustingly elegant. Only took 3 hours for me to come up with it

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

numeric_keypad = {
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

directional_keypad = {
    'A': (2, 0),
    '^': (1, 0),
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1),
}

caches = []
# Should equal the number of directional keypads that robots are using
NUM_CACHES = 25

def main():
    total = 0

    for _ in range(NUM_CACHES):
        caches.append({})

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
    # When entering a character, we know the directional keypad (and all keypads down the hierarchy)
    # must end at 'A'. This lets us chunk out the problem
    return cache_sequence(code, 0, numeric_keypad)

def cache_sequence(sequence, cache_index, keypad):
    if cache_index >= len(caches):
        return get_shortest_sequence(sequence, keypad)

    sequences = get_possible_sequences(sequence, keypad)
    cache = caches[cache_index]
    min_sequence_length = sys.maxsize

    for sequence in sequences:
        chunks = break_into_chunks(sequence)
        total = 0
        for chunk in chunks:
            if chunk not in cache:
                cache[chunk] = cache_sequence(chunk, cache_index + 1, directional_keypad)
            total += cache[chunk]
        if total < min_sequence_length:
            min_sequence_length = total
    return min_sequence_length

def break_into_chunks(sequence):
    next_chunk = ""
    chunks = []
    for ch in sequence:
        next_chunk += ch
        if ch == "A":
            chunks.append(next_chunk)
            next_chunk = ""
    if len(next_chunk):
        chunks.append(next_chunk)
    return chunks

def get_shortest_sequence(sequence, keypad):
    possible_sequences = get_possible_sequences(sequence, keypad)
    min_sequence_length = sys.maxsize
    for sequence in possible_sequences:
        if len(sequence) < min_sequence_length:
            min_sequence_length = len(sequence)
    return min_sequence_length

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

def get_possible_sequences(code, keypad):
    initial_pos = keypad['A']
    sequences = set()
    # Explore all possibilities
    q = deque()
    q.append((code, initial_pos, ""))
    visited = set()
    while len(q):
        key = q.pop()
        if key in visited:
            continue
        visited.add(key)

        remaining_code, pos, sequence_so_far = key
        if len(remaining_code) <= 0:
            sequences.add(sequence_so_far)
            continue
        # The shortest path will always be moving first on one axis, then the other
        # There are points of ambiguity where either could work
        next_ch = remaining_code[0]
        next_pos = keypad[next_ch]

        # Optimization: If at the same position, no need to move
        if pos == next_pos:
            q.append((remaining_code[1:], next_pos, sequence_so_far + "A"))
            continue

        definitely_horizontal_first = pos[1] == next_pos[1] or (pos[0], next_pos[1]) not in keypad.values()
        definitely_vertical_first = pos[0] == next_pos[0] or (next_pos[0], pos[1]) not in keypad.values()
        ambiguous = not definitely_horizontal_first and not definitely_vertical_first
        if not ambiguous:
            assert definitely_vertical_first ^ definitely_horizontal_first

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

if __name__ == "__main__":
    main()