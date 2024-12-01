import sys, os, itertools as itt
from collections import deque # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

walls = set()
startPos = None
sizeY = len(lines)
sizeX = len(lines[0])

maxPath = -1

def get_longest_path(graph, pos, visited, pathLength):
    global maxPath
    candidates = []
    visited.add(pos)
    for neighbor in graph[pos]:
        if neighbor[0] not in visited:
            candidates.append(neighbor)
    if len(candidates) == 0:
        if pos[1] == sizeY - 1:
            if pathLength > maxPath:
                #print(pathLength)
                maxPath = pathLength
            return pathLength
        return -1
    
    longestCandidate = 0
    for candidate in candidates:
        (nextNode, pathToNode) = candidate
        longestCandidate = max(longestCandidate, get_longest_path(graph, nextNode, visited.copy(), pathLength + pathToNode))
    return longestCandidate

def print_path(path):
    for y in range(sizeY):
        s = ""
        for x in range(sizeX):
            if (x, y) in walls:
                s += "#"
            elif (x, y) in path:
                s += "O"
                i += 1
            else:
                s += "."
        print(s)
        
def simplify_paths(startPos):
    q = deque()
    q.append((startPos, startPos))
    v = set()
    graph = {}
    while q:
        (start, connector) = q.popleft()
        pos = start
        pathLength = 0
        
        if start != connector:
            pathLength += 1
        
        while True:
            v.add(pos)
            candidates = []
            for direction in CARDINAL_NEIGHBORS:
                nextPos = addT(pos, direction)
                if nextPos in walls or nextPos in v or not in_bounds(nextPos, sizeY, sizeX):
                    continue
                candidates.append(nextPos)
            if len(candidates) == 1:
                pos = candidates[0]
                pathLength += 1
            elif len(candidates) == 0:
                break
            else:
                nextStart = pos
                for candidate in candidates:
                    q.append((candidate, nextStart))
                break
        end = pos 
        if connector not in graph:
            graph[connector] = []
        if end not in graph:
            graph[end] = []
        graph[connector].append((end, pathLength))
        graph[end].append((connector, pathLength))
    
    return graph

def main():
    y = 0
    for line in lines:
        x = 0
        for ch in line:
            if ch == "#":
                walls.add((x, y))
            else:
                if y == 0:
                    startPos = (x, y)
            x += 1
        y += 1
    
    graph = simplify_paths(startPos)
    longestPath = get_longest_path(graph, startPos, set(), 0)
    # Subtract 1 for the start node
    print(longestPath)

if __name__ == "__main__":
    main()