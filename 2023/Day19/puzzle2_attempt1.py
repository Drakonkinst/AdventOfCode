import sys, os, itertools as itt
import random
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

xmas = "xmas"
finish = "AR"

flows = {}
boundaries = [set() for _ in range(len(xmas))]

def test(part):
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
    return curr == "A"

def main():
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
                varIndex = xmas.index(var)
                rules.append((op, destination, varIndex, val))
                
                boundaries[varIndex].add(val)
                if op == "<":
                    boundaries[varIndex].add(val - 1)
                else:
                    boundaries[varIndex].add(val + 1)
            else:
                destination = rule
                rules.append(("switch", destination))
        flows[name] = rules
        index += 1
        
    for i in range(len(boundaries)):
        boundaries[i].add(1)
        boundaries[i].add(4001)
        boundaries[i] = list(boundaries[i])
        boundaries[i].sort()
    
    allX = boundaries[0]    
    allM = boundaries[1]    
    allA = boundaries[2]    
    allS = boundaries[3]    
    
    print(boundaries)
    print([len(x) for x in boundaries])
    total = 0
    a = 0
    for xi, x in enumerate(allX):
        if xi == len(allX) - 1:
            continue
        print("x", xi)
        xInterval = allX[xi + 1] - x
        for mi, m in enumerate(allM):
            if mi == len(allM) - 1:
                continue
            mInterval = allM[mi + 1] - m
            print("m", mi)
            for ai, a in enumerate(allA):
                if ai == len(allA) - 1:
                    continue
                aInterval = allA[ai + 1] - a
                for si, s in enumerate(allS):
                    if si == len(allS) - 1:
                        continue
                    if test([x, m, a, s]):
                        sInterval = allS[si + 1] - s
                        amount = xInterval * mInterval * aInterval * sInterval
                        total += amount
    print(total)

if __name__ == "__main__":
    main()