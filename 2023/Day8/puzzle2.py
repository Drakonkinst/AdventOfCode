import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

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
    
    # Find the first step each one reaches "Z"
    # This is the cycle, if the first step is N then it will reach Z again every N cycles
    while True:
        i = instr[step % len(instr)]
        index = 1 if i == "R" else 0
        for j in range(len(nodes)):
            nodes[j] = m[nodes[j]][index]
            if nodes[j].endswith("Z"):
                if first[j] < 0:
                    # We had steps start at 0 to correspond with instruction,
                    # the actual one should be +1
                    first[j] = step + 1
        
        # Check that all the first array is fully populated
        anyNegative = False
        for f in first:
            if f < 0:
                anyNegative = True
                break
        if not anyNegative:
            break
            
        step += 1
    
    # Get least common multiple of all the cycles
    # This represents when the cycles will coincide
    lcm = first[0]
    for f in first[1:]:
        lcm = math.lcm(f, lcm)
    print(lcm)

if __name__ == "__main__":
    main()