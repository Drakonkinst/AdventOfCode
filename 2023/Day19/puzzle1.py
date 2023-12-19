import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

xmas = "xmas"
finish = "AR"

def main():
    index = 0
    flows = {}
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
                rules.append((op, destination, xmas.index(var), val))
            else:
                destination = rule
                rules.append(("switch", destination))
        flows[name] = rules
        index += 1
    
    index += 1
    parts = []
    while index < len(lines):
        line = lines[index]
        parts.append(positive_ints(line))
        index += 1
    
    total = 0
    for part in parts:
        curr = "in"
        while curr not in finish:
            flow = flows[curr]
            for rule in flow:
                if rule[0] == "switch":
                    curr = rule[1]
                    break
                else:
                    op = rule[0]
                    varIndex = rule[2]
                    val = rule[3]
                    if op == "<":
                        if part[varIndex] < val:
                            curr = rule[1]
                            break
                    elif op == ">":
                        if part[varIndex] > val:
                            curr = rule[1]
                            break
        if curr == "A":
            total += sum(part)
        
    print(total)

if __name__ == "__main__":
    main()