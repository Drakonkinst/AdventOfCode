import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

xmas = "xmas"
finish = "AR"

flows = {}

# Different approach, with help from Reddit

def count(name, ranges):
    if name == "R":
        return 0
    if name == "A":
        return math.prod([hi - lo + 1 for lo, hi in ranges.values()])
    
    total = 0
    rules = flows[name]
    for rule in rules:
        op = rule[0]
        outcome = rule[1]
        if op == "switch":
            total += count(outcome, ranges)
        else:
            ranges_copy = ranges.copy()
            var = rule[2]
            val = rule[3]
            varRange = ranges[var]
            if varRange[0] < val < varRange[1]:
                if op == "<":
                    ranges_copy[var] = (varRange[0], val - 1)
                    ranges[var] = (val, varRange[1])
                else:
                    ranges_copy[var] = (val + 1, varRange[1])
                    ranges[var] = (varRange[0], val)
                total += count(outcome, ranges_copy)
    return total

def main():
    # Parse all rules
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line:
            break
        openBrace = line.index("{")
        name = line[:openBrace]
        ruleStrs = line[openBrace + 1 : -1].split(",")
        rules = []
        for rule in ruleStrs:
            if ":" in rule:
                colon = rule.index(":")
                var = rule[0]
                op = rule[1]
                val = int(rule[2:colon])
                destination = rule[colon + 1:]
                rules.append([op, destination, var, val])
            else:
                destination = rule
                rules.append(["switch", destination])
        flows[name] = rules
        index += 1
    result = count("in", {k: (1, 4000) for k in xmas})
    print(result)

if __name__ == "__main__":
    main()