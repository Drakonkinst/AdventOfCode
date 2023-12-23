import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]
grid = lines
numRows = len(grid)
numCols = len(grid[0])
allVisited = set()

def find_in_grid(grid, ch):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == ch:
                return (row, col)
    assert False

def get(row, col):
    # Works for negatives too, thankfully
    (row, col) = modulo(row, col)
    return grid[row][col]
    
def modulo(row, col):
    return (row % len(grid), col % len(grid[0]))

def in_bounds(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

cache = {}

def calc(stepsSoFar, maxSteps, startRow, startCol):
    cacheKey = (stepsSoFar % 2 == 0, startRow, startCol)
    if cacheKey in cache:
        print("CACHE HIT")
        stepsRequired, minStepsToEdges, count = cache[cacheKey]
        if maxSteps >= stepsRequired:
            return minStepsToEdges, count, []
    
    q = deque()
    q.append((0, startRow, startCol))
    visited = set()
    canReach = set()
    
    minStepsToEdges = {k: math.inf for k in CARDINAL_NEIGHBORS}
    
    maxStepForCell = 0
    while q:
        (step, row, col) = q.popleft()
        key = (row, col)
        if key in visited:
            continue
        visited.add(key)
        
        maxStepForCell = max(maxStepForCell, step)
        if (stepsSoFar + step) % 2 == maxSteps % 2:
            canReach.add((row, col))
        
        if step >= maxSteps:
            continue
        
        for (offsetCol, offsetRow) in CARDINAL_NEIGHBORS:
            nextRow = row + offsetRow
            nextCol = col + offsetCol
            if not in_bounds(nextRow, nextCol, grid):
                minStepsToEdges[(offsetCol, offsetRow)] = min(minStepsToEdges[(offsetCol, offsetRow)], step + 1)
                continue
            if grid[nextRow][nextCol] == "#":
                continue
            q.append((step + 1, nextRow, nextCol))
    
    if all(not math.isinf(x) for x in minStepsToEdges.values()):
        cache[cacheKey] = (max(minStepsToEdges.values()), minStepsToEdges, len(canReach))
    
    return minStepsToEdges, len(canReach), canReach

def main():
    grid = lines
    startRow, startCol = find_in_grid(grid, "S")
    
    maxSteps = 10
    
    #print(calc(0, 1, 10, 5))
    #return
    
    q = deque()
    q.append((0, maxSteps, 0, 0, startRow, startCol))
    v = set()
    total = 0
    while q:
        stepsSoFar, stepsRemaining, cellX, cellY, row, col = q.popleft()
        if stepsRemaining <= 0:
            continue
        if (cellX, cellY) in v:
            continue
        v.add((cellX, cellY))
        minStepsToEdges, stepsInCell, canReach = calc(stepsSoFar, stepsRemaining, row, col)
        for (r, c) in canReach:
            allVisited.add((cellY * numRows + r, cellX * numCols + c))
        #if stepsInCell >= maxForAnyCell:
        print((stepsSoFar, stepsRemaining, cellX, cellY, row, col), "->", stepsInCell, minStepsToEdges)
        total += stepsInCell
        for edge in minStepsToEdges:
            if not math.isinf(minStepsToEdges[edge]):
                nextStartRow = (-edge[1] + 1) * (numRows // 2)
                nextStartCol = (-edge[0] + 1) * (numCols // 2)
                q.append((stepsSoFar + minStepsToEdges[edge], stepsRemaining - minStepsToEdges[edge], cellX + edge[0], cellY + edge[1], nextStartRow, nextStartCol))
    print(total)
    l = list(allVisited)
    l.sort()
    print(l)
    
if __name__ == "__main__":
    main()