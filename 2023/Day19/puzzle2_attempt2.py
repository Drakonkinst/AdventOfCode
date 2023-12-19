import sys, os, itertools as itt
import threading
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

xmas = "xmas"
finish = "AR"

flows = {}

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
    # Parse all rules
    index = 0
    numRefs = {}
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
                rules.append([op, destination, varIndex, val])
                if destination not in numRefs:
                    numRefs[destination] = 0
                numRefs[destination] += 1
            else:
                destination = rule
                rules.append(["switch", destination])
                if destination not in numRefs:
                    numRefs[destination] = 0
                numRefs[destination] += 1
        flows[name] = rules
        index += 1
    
    # Remove rules that are all accept or all reject
    # And simplify them into existing rules
    allAccepts = set()
    allRejects = set()
    anyChanges = True
    while anyChanges:
        anyChanges = False
        toRemove = set()
        for name in flows:
            allReject = True
            allAccept = True
            for rule in flows[name]:
                destination = rule[1]
                if destination in allAccepts:
                    rule[1] = "A"
                elif destination in allRejects:
                    rule[1] = "R"
                destination = rule[1]
                if destination != "A":
                    allAccept = False
                if destination != "R":
                    allReject = False
            if allAccept:
                allAccepts.add(name)
                toRemove.add(name)
                anyChanges = True
            elif allReject:
                allRejects.add(name)
                toRemove.add(name)
                anyChanges = True
        for k in toRemove:
            del flows[k]
    print("Skipped", len(allAccepts), "+", len(allRejects), "flows") 
    
    # Combine all rules so that all rules end with an "A" or "R"
    q = deque()
    done = set()
    for name in flows:
        q.append(name)
    while q:
        name = q.pop()
        if name in done:
            continue
        rules = flows[name]
        outcome = rules[-1][1]
        if outcome in finish:
            done.add(name)
            continue
        if outcome in done:
            del rules[-1]
            rules.extend(flows[outcome].copy())
            numRefs[outcome] -= 1
            done.add(name)
            continue
        q.append(name)
        q.append(outcome)
    
    # Remove rules that are no longer referenced
    numDeref = 0
    for name in numRefs:
        if numRefs[name] <= 0:
            numDeref += 1
            del flows[name]
    print(numDeref, "flows dereferenced")
    
    # Merge rule terms: Combine like comparisons
    skipped = 0
    for name in flows:
        lastVarIndex = -1
        lastOp = ""
        lastOutcome = ""
        lastVal = -1
        index = 0
        rules = flows[name]
        while index < len(rules):
            rule = rules[index]
            op = rule[0]
            if op == "switch":
                break
            outcome = rule[1]
            varIndex = rule[2]
            val = rule[3]
            if lastVarIndex == varIndex and lastOp == op and lastOutcome == outcome:
                # Matches, try to merge by deleting the current
                if op == "<":
                    if val < lastVal:
                        rules[-1][3] = val
                    else:
                        val = lastVal
                if op == ">":
                    if val > lastVal:
                        rules[-1][3] = val
                    else:
                        val = lastVal
                # Delete current
                skipped += 1
                del rules[index]
                index -= 1
            lastVarIndex = varIndex
            lastOp = op
            lastOutcome = outcome
            lastVal = val
            index += 1
    
    skipped2 = 0
    for name in flows:
        rules = flows[name]
        lastOp = rules[-1][1]
        index = len(rules) - 2
        while index >= 0:
            rule = rules[index]
            if rule[1] == lastOp:
                del rules[index]
                skipped2 += 1
            else:
                break
            index -= 1
    print("Skipped", skipped, "+", skipped2, "rules")
    for k in flows:
        print(k, flows[k])
    
    # Gather boundaries from the remaining flows and rules
    boundaries = [set() for _ in range(len(xmas))]
    for name in flows:
        for rule in flows[name]:
            op = rule[0]
            if op == "switch":
                continue
            varIndex = rule[2]
            val = rule[3]
            boundaries[varIndex].add(val)
            if op == "<":
                boundaries[varIndex].add(val - 1)
            else:
                boundaries[varIndex].add(val + 1)
    
    for i in range(len(boundaries)):
        boundaries[i].add(1)
        boundaries[i].add(4001)
        boundaries[i] = list(boundaries[i])
        boundaries[i].sort()
    
    allX = boundaries[0]    
    allM = boundaries[1]    
    allA = boundaries[2]    
    allS = boundaries[3]    
    
    print([len(x) for x in boundaries])
    total = 0
    a = 0
    for xi, x in enumerate(allX[:-1]):
        print("x", xi)
        xInterval = allX[xi + 1] - x
        for mi, m in enumerate(allM[:-1]):
            mInterval = allM[mi + 1] - m
            for ai, a in enumerate(allA[:-1]):
                aInterval = allA[ai + 1] - a
                for si, s in enumerate(allS[:-1]):
                    if test([x, m, a, s]):
                        sInterval = allS[si + 1] - s
                        amount = xInterval * mInterval * aInterval * sInterval
                        total += amount
    print(total)

if __name__ == "__main__":
    main()