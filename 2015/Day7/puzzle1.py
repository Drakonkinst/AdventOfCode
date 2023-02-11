import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def parseSimple(x):
    if x.isnumeric():
        return int(x)
    return x

def parse(x):
    w = words(x)
    if len(w) == 1:
        if x.isnumeric():
            return int(w[0])
        return {
            "op": "ID",
            "args": [w[0]]
        }
    if len(w) == 2:
        return {
            "op": "NOT",
            "args": [parseSimple(w[1])]
        }
    # len == 3
    return {
        "op": w[1],
        "args": [parseSimple(w[0]), parseSimple(w[2])]
    }

def main():
    l = {}
    for line in lines:
        w = words(line)
        var = w[-1]
        arrowIndex = line.index("->")
        val = parse(line[0:arrowIndex - 1])
        l[var] = val
        
    # Assume no circular
    q = deque()
    target = "a"
    q.append(target)
    v = set()
    while len(q) > 0:
        var = q.pop()
        v.add(var)
        data = l[var]
        if isinstance(data, int):
            continue
        op = data["op"]
        args = data["args"]
        argVals = []
        toAdd = []
        good = True
        for a in args:
            if isinstance(a, int):
                argVals.append(a)
            else:
                if isinstance(l[a], int):
                    argVals.append(l[a])
                else:
                    toAdd.append(a)
                    good = False
        if not good:
            q.append(var)
            for x in toAdd:
                q.append(x)
            continue
        val = -1
        if op == "ID":
            val = argVals[0]
        elif op == "NOT":
            val = ~argVals[0]
        elif op == "AND":
            val = argVals[0] & argVals[1]
        elif op == "OR":
            val = argVals[0] | argVals[1]
        elif op == "LSHIFT":
            val = argVals[0] << argVals[1]
        elif op == "RSHIFT":
            val = argVals[0] >> argVals[1]
        else:
            assert False
        print(var, argVals, op, val)
        l[var] = val
            
    print(l[target])
    
if __name__ == "__main__":
    main()