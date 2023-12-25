import sys, os, itertools as itt
from collections import deque # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
import networkx as nx 
import matplotlib.pyplot as plt 
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def remove(graph, a, b):
    graph[a].remove(b)
    graph[b].remove(a)

# VERY hacky solution, where I just visualize the graph, snip them manually,
# then calculate the size of one group to automatically get the other.
# Would like to figure out how to do this better...later
def main():
    total = 0
    graph = {}
    edges = []
    G = nx.Graph()
    for line in lines:
        name, others = line.split(":")
        others = words(others.strip())
        if name not in graph:
            graph[name] = set()
        for o in others:
            graph[name].add(o)
            edges.append([name, o])
            if o not in graph:
                graph[o] = set()
            graph[o].add(name)
    
    # Visualize to figure out which 3 nodes to snip by hand
    # G.add_edges_from(edges)
    # nx.draw_networkx(G)
    # plt.show()
    
    numNodes = len(graph)
    # remove(graph, "cmg", "bvb")
    # remove(graph, "nvd", "jqt")
    # remove(graph, "pzl", "hfx")
    # start = "frs"
    # Part 1
    remove(graph, "czs", "tdk")
    remove(graph, "kbr", "bbg")
    remove(graph, "vtt", "fht")
    start = "lrn"
    
    # Get the size of one group by starting from a random node
    q = deque()
    v = set()
    q.append(start)
    
    while q:
        name = q.pop()
        if name in v:
            continue
        v.add(name)
        for nextNode in graph[name]:
            if nextNode not in v:
                q.append(nextNode)
    print(len(v), numNodes - len(v), len(v) * (numNodes - len(v)))

if __name__ == "__main__":
    main()