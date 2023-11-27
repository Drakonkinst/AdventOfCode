import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

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
    for name, node in nodes.items():
        if node["parent"] == None:
            print(name)
            return
    print("FAIL")

if __name__ == "__main__":
    main()