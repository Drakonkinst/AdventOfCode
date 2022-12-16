from copy import deepcopy
import sys
from collections import deque

MAX_STEP = 26

def findMax(edges, rates, start):
    q = deque()
    openedAtStart = set()
    # Optimization #2: Mark 0 rate valves as opened
    for k, v in rates.items():
        if v == 0:
            openedAtStart.add(k)
    
    # Current node, current score, list of opened, step
    q.append((start, start, 0, openedAtStart, 1, True, False))
    maxScore = -sys.maxsize
    lastStep = 0
    highScoreAtState = {}
    anyAllValvesOpenStep = sys.maxsize
    bestRatePerStep = {}
    
    while len(q) > 0:
        node, eNode, score, opened, step, isYou, allValvesOpen = q.popleft()
        
        if not allValvesOpen and step * 2 + (0 if isYou else 1) >= anyAllValvesOpenStep:
            continue
            
        if step > lastStep:
            print(step, len(q), anyAllValvesOpenStep)
            lastStep = step
        
        # Check max depth
        if step > MAX_STEP:
            break
        
        if isYou:
            # Calculate new score increase - only happens on Your turn
            for x in opened:
                score += rates[x]
            if score > maxScore:
                maxScore = score
            
            newStep = step # Step should stay the same
            
            # Optimization #1: Skip if already higher score found at this configuration
            if (node, eNode, step) in highScoreAtState:
                if highScoreAtState[(node, eNode, step)] >= score:
                    continue
            highScoreAtState[(node, eNode, step)] = score
            
            if allValvesOpen:
                # If we do nothing
                q.append((node, eNode, score, opened, newStep, not isYou, allValvesOpen))
            else:
                # If we open the current
                if node not in opened:
                    newOpened = set(opened)
                    newOpened.add(node)
                    allValvesOpen = len(newOpened) >= len(rates)
                    if allValvesOpen:
                        anyAllValvesOpenStep = min(newStep * 2, anyAllValvesOpenStep)
                    q.append((node, eNode, score, newOpened, newStep, not isYou, allValvesOpen))
                
                # If we move to neighbors
                for x in edges[node]:
                    q.append((x, eNode, score, opened, newStep, not isYou, allValvesOpen))
        else:
            # Increment step: Only happens on Elephant turn
            newStep = step + 1
            
            if allValvesOpen:
                # If we do nothing
                q.append((node, eNode, score, opened, newStep, not isYou, allValvesOpen))
            else:
                # If we open the current
                if eNode not in opened:
                    newOpened = set(opened)
                    newOpened.add(eNode)
                    allValvesOpen = len(newOpened) >= len(rates)
                    if allValvesOpen:
                        anyAllValvesOpenStep = min(newStep * 2 + 1, anyAllValvesOpenStep)
                    q.append((node, eNode, score, newOpened, newStep, not isYou, allValvesOpen))
                
                # If we move to neighbors
                for x in edges[eNode]:
                    q.append((node, x, score, opened, newStep, not isYou, allValvesOpen))
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