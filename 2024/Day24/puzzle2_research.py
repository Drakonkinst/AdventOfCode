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
    original_wire_values = {}
    solution_wires = set()
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line:
            break
        wire_name = line[:3]
        add_if_solution_wire(solution_wires, wire_name)
        wire_value = line[5] == '1'
        original_wire_values[wire_name] = (wire_value, None)
        index += 1

    operation_counts = {
        "AND": 0,
        "OR": 0,
        "XOR": 0
    }
    index += 1
    while index < len(lines):
        line = lines[index]
        w = words(line)
        input_1 = w[0]
        input_2 = w[2]
        operation = w[1]
        operation_counts[operation] += 1
        output_wire = w[4]
        add_if_solution_wire(solution_wires, input_1)
        add_if_solution_wire(solution_wires, input_2)
        add_if_solution_wire(solution_wires, output_wire)
        original_wire_values[output_wire] = (None, (input_1, input_2, operation))
        index += 1

    # Identify all output wires that are incorrect with a minimal example
    print(operation_counts)
    problem_outputs = test_each_input(original_wire_values, solution_wires)
    print(len(problem_outputs), problem_outputs)
    for problem_wire in problem_outputs:
        problem_inputs = get_inputs_for_output(problem_wire, original_wire_values)
        # print(problem_wire, len(problem_inputs), problem_inputs)

    valid_swaps = set()
    # Ideally, 4 pairs but this might work
    for outputs in itt.permutations(problem_outputs):
        pass


def get_inputs_for_output(output_wire, wire_values):
    q = deque()
    q.append(output_wire)
    inputs = set()
    while len(q):
        problem_wire = q.pop()
        if problem_wire in inputs:
            continue
        inputs.add(problem_wire)
        _, gate = wire_values[problem_wire]
        if gate is not None:
            input_1, input_2, _ = gate
            if input_1[0] != 'x' and input_1[0] != 'y':
                q.append(input_1)
            if input_2[0] != 'x' and input_2[0] != 'y':
                q.append(input_2)
    return inputs

def test_each_input(original_wire_values, solution_wires):
    problem_outputs = set()
    input_length = 45
    # Test (0, 0) in every position
    for i in range(input_length):
        wire_values = original_wire_values.copy()
        set_all_inputs_zero(wire_values)
        wire_number = str((input_length - i)).rjust(2, '0')
        wire_values = calculate(wire_values, solution_wires)
        if not is_correct_output(wire_values):
            problem_outputs.add("z" + wire_number)
    # Test (1, 0) in every position
    for i in range(input_length):
        wire_values = original_wire_values.copy()
        set_all_inputs_zero(wire_values)
        wire_number = str((input_length - i)).rjust(2, '0')
        wire_name = "x" + wire_number
        wire_values[wire_name] = (1, None)
        wire_values = calculate(wire_values, solution_wires)
        if not is_correct_output(wire_values):
            problem_outputs.add("z" + wire_number)
    # Test (0, 1) in every position
    for i in range(input_length):
        wire_values = original_wire_values.copy()
        set_all_inputs_zero(wire_values)
        wire_number = str((input_length - i)).rjust(2, '0')
        wire_name = "y" + wire_number
        wire_values[wire_name] = (1, None)
        wire_values = calculate(wire_values, solution_wires)
        if not is_correct_output(wire_values):
            problem_outputs.add("z" + wire_number)
    # Test (1, 1) in every position
    for i in range(input_length):
        wire_values = original_wire_values.copy()
        set_all_inputs_zero(wire_values)
        wire_number = str((input_length - i)).rjust(2, '0')
        wire_values["x" + wire_number] = (1, None)
        wire_values["y" + wire_number] = (1, None)
        wire_values = calculate(wire_values, solution_wires)
        if not is_correct_output(wire_values):
            problem_outputs.add("z" + wire_number)
    return problem_outputs

def is_correct_output(wire_values):
    x_str = wires_to_str("x", wire_values)
    y_str = wires_to_str("y", wire_values)
    z_str = wires_to_str("z", wire_values)
    x = int(x_str, 2)
    y = int(y_str, 2)
    z = int(z_str, 2)
    return x + y == z

def set_all_inputs_zero(wire_values):
    for wire_name in wire_values:
        if wire_name[0] == 'x' or wire_name[0] == 'y':
            wire_values[wire_name] = (0, None)

def calculate(wire_values, solution_wires):
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
    return wire_values

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