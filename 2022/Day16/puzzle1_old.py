from copy import deepcopy
import sys
from collections import deque

MAX_STEP = 30

def findMax(edges, rates, starts):
    q = deque()
    openedAtStart = set()
    # Optimization #2: Mark 0 rate valves as opened
    toOpen = []
    for k, v in rates.items():
        if v == 0:
            openedAtStart.add(k)
        else:
            toOpen.append(k)
    print("TO OPEN LEN:", len(toOpen))
    
    # Current node, current score, list of opened, step
    for n, c in starts:
        q.append((start, 0, openedAtStart, 1, 0))
    else:
        q.append((start, 0, openedAtStart, 1, 0))
    maxScore = -sys.maxsize
    lastStep = 0
    highScoreAtState = {}
    while len(q) > 0:
        node, score, opened, step, openedCode = q.popleft()
        
        if step > lastStep:
            print(step, len(q))
            lastStep = step
        
        # Check max depth
        if step > MAX_STEP:
            break
        
        # Calculate new score increase
        newScore = score
        for x in opened:
            newScore += rates[x]
        if newScore > maxScore:
            maxScore = newScore
        
        # Optimization #1: Skip if already higher score found at this configuration
        if (openedCode, node, step) in highScoreAtState:
            if highScoreAtState[(openedCode, node, step)] > newScore:
                continue
        highScoreAtState[(openedCode, node, step)] = newScore
        
        # If we do nothing
        q.append((node, newScore, opened, step + 1, openedCode))
        
        # If we open the current
        if node not in opened:
            newOpened = set(opened)
            newOpened.add(node)
            openedCode += 2 ** toOpen.index(node)
            q.append((node, newScore, newOpened, step + 1, openedCode))
        
        # If we move to neighbors
        for x in edges[node]:
            q.append((x, newScore, opened, step + 1, openedCode))
    return maxScore
    
def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    edges = {}
    rates = {}
    first = None
    zeroEdges = {}
    for line in lines:
        words = line.split(" ")
        name = words[1]
        rate = int(words[4][len("rate="):-1])
        edge = "".join(words[9:]).split(",")
        
        if first is None:
            first = name
        if rate == 0:
            zeroEdges[name] = edge
        else:
            edges[name] = [(x, 1) for x in edge]
        rates[name] = rate
        
    # Optimization: Eliminate 0 edges
    for k, v in edges.items():
        newEdges = []
        allEdges = v
        while len(allEdges) > 0:
            n, c = allEdges.pop()
            if n in zeroEdges:
                for x in zeroEdges[n]:
                    allEdges.append((x, c + 1))
            else:
                newEdges.append((n, c))
        edges[k] = newEdges
    
    best = findMax(edges, rates, first, zeroEdges)
    print("BEST", best)

if __name__ == "__main__":
    main()