from copy import deepcopy
import sys
from collections import deque

MAX_STEP = 30

def findMax(edges, rates, start):
    q = deque()
    openedAtStart = set()
    # Optimization #2: Mark 0 rate valves as opened
    for k, v in rates.items():
        if v == 0:
            openedAtStart.add(k)
    
    # Current node, current score, list of opened, step
    q.append((start, 0, openedAtStart, 1))
    maxScore = -sys.maxsize
    lastStep = 0
    highScoreAtState = {}
    while len(q) > 0:
        node, score, opened, step = q.popleft()
        
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
        if (node, step) in highScoreAtState:
            if highScoreAtState[(node, step)] > newScore:
                continue
        highScoreAtState[(node, step)] = newScore
        
        # If we do nothing
        q.append((node, newScore, opened, step + 1))
        
        # If we open the current
        if node not in opened:
            newOpened = set(opened)
            newOpened.add(node)
            q.append((node, newScore, newOpened, step + 1))
        
        # If we move to neighbors
        for x in edges[node]:
            q.append((x, newScore, opened, step + 1))
    return maxScore
    
def main():
    file = open("input.txt", "r");
    lines = [line.strip() for line in file.readlines()]
    
    edges = {}
    rates = {}
    for line in lines:
        words = line.split(" ")
        name = words[1]
        rate = int(words[4][len("rate="):-1])
        edge = "".join(words[9:]).split(",")

        edges[name] = edge
        rates[name] = rate
    
    best = findMax(edges, rates, "AA")
    print("BEST", best)

if __name__ == "__main__":
    main()