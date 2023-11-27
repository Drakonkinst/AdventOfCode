import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

# The code is so bad here I apologize
def is_balanced(node, sumWeights):
    if len(node["children"]) == 0:
        return True

    value = sumWeights[node["children"][0]]
    for child in node["children"]:
        if sumWeights[child] != value:
            return False
    return True

def main():
    # Read input
    nodes = {}
    for line in lines:
        w = words(line)
        name = w[0]
        weight = int(w[1][1:-1])
        
        node = {
            "name": name,
            "weight": weight,
            "children": [],
            "parent": None
        }
        
        index = 3
        while index < len(w):
            child = w[index]
            if index < len(w) - 1:
                child = child[:-1]
            node["children"].append(child)
            index += 1
        
        nodes[name] = node
    
    # Process children
    for name, node in nodes.items():
        for child in node["children"]:
            nodes[child]["parent"] = name
    
    # Find the node without a parent
    root = None
    for name, node in nodes.items():
        if node["parent"] == None:
            root = name
    
    # Iteratively calculate weight of entire tree
    sumWeights = {}
    q = deque([root])
    while len(q) > 0:
        curr = q.pop()
        node = nodes[curr]

        toAdd = []
        total = node["weight"]
        for child in node["children"]:
            if child not in sumWeights:
                toAdd.append(child)
            else:
                total += sumWeights[child]
        if len(toAdd) > 0:
            q.append(curr)
            for child in toAdd:
                q.append(child)
        else:
            sumWeights[curr] = total
    
    # Identify unbalanced section
    curr = root
    prev = None
    badNode = None
    while True:
        if is_balanced(node, sumWeights):
            badNode = prev
            break
        node = nodes[curr]
        weights = [sumWeights[child] for child in node["children"]]
        counts = Counter(weights)
        oddValue = min(counts, key=counts.get)
        oddChild = node["children"][weights.index(oddValue)]
        prev = curr
        curr = oddChild
    print(badNode)
    
    # Get value needed to fix weight
    baseWeight = nodes[badNode]["weight"]
    parent = nodes[badNode]["parent"]
    parentNode = nodes[parent]
    for child in parentNode["children"]:
        if child != badNode:
            correctValue = sumWeights[child]
            newBaseWeight = baseWeight + correctValue - sumWeights[badNode]
            print("ANS", newBaseWeight)
            return
    print("FAIL")


if __name__ == "__main__":
    main()