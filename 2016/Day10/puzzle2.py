import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    bots = {}
    outputs = {}
    rules = {}
    q = deque()

    for line in lines:
        vals = ints(line)
        if line.startswith("value"):
            val = vals[0]
            botId = vals[1]
            if botId in bots:
                q.append((botId, val))
            else:
                bots[botId] = val
        elif line.startswith("bot"):
            w = words(line)
            isOutput1 = w[5] == "output"
            isOutput2 = w[10] == "output"
            botId = vals[0]
            id1 = vals[1]
            id2 = vals[2]
            
            if isOutput1:
                outputs[id1] = []
            if isOutput2:
                outputs[id2] = []
            
            rules[botId] = (isOutput1, id1, isOutput2, id2)
    
    while len(q) > 0:
        botId, val1 = q.popleft()
        if botId not in bots:
            bots[botId] = None
        val2 = bots[botId]
        
        if val2 == None:
            bots[botId] = val1
            continue
        
        if val1 > val2:
            val1, val2 = val2, val1
        
        bots[botId] = None
        isOutput1, id1, isOutput2, id2 = rules[botId]
        if isOutput1:
            outputs[id1].append(val1)
        else:
            q.append((id1, val1))
        
        if isOutput2:
            outputs[id2].append(val2)
        else:
            q.append((id2, val2))
    print(outputs[0][0] * outputs[1][0] * outputs[2][0])

if __name__ == "__main__":
    main()