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
    wire_values = {}
    solution_wires = set()
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line:
            break
        wire_name = line[:3]
        add_if_solution_wire(solution_wires, wire_name)
        wire_value = line[5] == '1'
        wire_values[wire_name] = (wire_value, None)
        index += 1

    index += 1
    while index < len(lines):
        line = lines[index]
        w = words(line)
        input_1 = w[0]
        input_2 = w[2]
        operation = w[1]
        output_wire = w[4]
        add_if_solution_wire(solution_wires, input_1)
        add_if_solution_wire(solution_wires, input_2)
        add_if_solution_wire(solution_wires, output_wire)
        wire_values[output_wire] = (None, (input_1, input_2, operation))
        index += 1

    q = deque()
    for solution_wire in solution_wires:
        q.append(solution_wire)

    while len(q):
        wire_name = q.pop()
        resolved, gate = wire_values[wire_name]
        if resolved is not None:
            # Already resolved
            continue
        input_1, input_2, operation = gate
        input_1_value = wire_values[input_1][0]
        input_2_value = wire_values[input_2][0]
        need_to_wait = input_1_value is None or input_2_value is None
        if need_to_wait:
            q.append(wire_name)
            if input_1_value is None:
                q.append(input_1)
            if input_2_value is None:
                q.append(input_2)
            continue

        # At this point, both inputs should be present
        wire_value = get_result(input_1_value, input_2_value, operation)
        wire_values[wire_name] = (wire_value, None)

    solution_str = wires_to_str("z", wire_values)
    solution = int(solution_str, 2)
    print(solution)

def wires_to_str(prefix, wire_values):
    wires = []
    for wire_name in wire_values:
        if wire_name.startswith(prefix):
            wires.append(wire_name)
    wires.sort()
    wires.reverse()
    wires_str = ""
    for wire in wires:
        wire_value = wire_values[wire][0]
        if wire_value is None:
            assert False
        wires_str += '1' if wire_value else '0'
    return wires_str

def get_result(input_1_value, input_2_value, operation):
    if operation == "AND":
        return input_1_value and input_2_value
    elif operation == "OR":
        return input_1_value or input_2_value
    elif operation == "XOR":
        return input_1_value != input_2_value
    else:
        assert False

def add_if_solution_wire(solution_wires, wire_name):
    if wire_name[0] == 'z':
        solution_wires.add(wire_name)

if __name__ == "__main__":
    main()