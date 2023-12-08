import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def done(nodes, adds, index):
    good = True
    for i in range(len(nodes)):
        node = nodes[i]
        if node.endswith("Z"):
            adds[i].append(index)
        else:
            good = False
    return good
            
def main():
    instr = lines[0]
    
    m = {}
    nodes = []
    for line in lines[2:]:
        w = words(line)
        parent = w[0]
        left = w[2][1:-1]
        right = w[3][:-1]
        m[parent] = (left, right)
        if parent.endswith("A"):
            nodes.append(parent)
    
    step = 0
    first = [-1 for _ in range(len(nodes))]
    while True:
        i = instr[step % len(instr)]
        index = 1 if i == "R" else 0
        for j in range(len(nodes)):
            nodes[j] = m[nodes[j]][index]
            if nodes[j].endswith("Z"):
                if first[j] < 0:
                    first[j] = step + 1
        
        anyNegative = False
        for f in first:
            if f < 0:
                anyNegative = True
                break
        if not anyNegative:
            break
            
        step += 1
    
    # Get least common multiple of all the cycles
    lcm = first[0]
    for f in first[1:]:
        lcm = math.lcm(f, lcm)
    print(lcm)

if __name__ == "__main__":
    main()