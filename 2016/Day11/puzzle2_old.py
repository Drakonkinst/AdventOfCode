import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def validate_floor(floor):
    dangerous = False
    exposed = False
    for item in floor:
        isGenerator = item.endswith("G")
        if isGenerator:
            dangerous = True
        else:
            generator = item + "G"
            if generator not in floor:
                exposed = True
    return not exposed or not dangerous

def is_dangerous(floor):
    for item in floor:
        isGenerator = item.endswith("G")
        if isGenerator:
            return True
    return False

def hash_data(floorData, allItems):
    return (
        hash_floor(floorData[0], allItems),
        hash_floor(floorData[1], allItems),
        hash_floor(floorData[2], allItems)
    )

# def hash_floor(floor, allItems):
#     total = 0
#     pair = 0
#     for item in floor:
#         isGenerator = item.endswith("G")
#         if isGenerator:
#             chip = item[:-1]
#             if chip in floor:
#                 continue
#         else:
#             generator = item + "G"
#             if generator in floor:
#                 pair += 1
#                 continue
#         val = allItems.index(item)
#         total += 2 ** val
#     return total, pair
    
def hash_floor(floor, allItems):
    total = 0
    for item in floor:
        val = allItems.index(item)
        total += 2 ** val
    return total

def first_nonempty(floorData):
    for i in range(len(floorData)):
        if len(floorData[i]) > 0:
            return i
    return -1

def main():
    floors = []
    maxItems = 0
    allItems = []
    for i in range(4):
        items = []
        w = words(lines[i])
        j = 0
        while j < len(w):
            word = w[j]
            if word != "a":
                j += 1
                continue
            first = w[j + 1]
            second = w[j + 2]

            if second.startswith("generator"):
                element = first
                items.append(element + "G")
            elif second.startswith("microchip"):
                nextDash = first.index("-")
                element = first[:nextDash]
                items.append(element)
            
            j += 3
        
        if len(floors) == 0:
            items = items + ["elerium", "eleriumG", "dilithium", "dilithiumG"]
        floors.append(items)
        maxItems += len(items)
        for item in items:
            if item not in allItems:
                allItems.append(item)
    
    q = deque([(0, 0, floors)])
    lastStep = -1
                
    v = set()
    while len(q) > 0:
        floorNum, step, floorData = q.popleft()
        state = (floorNum, hash_data(floorData, allItems))
        
        if state in v:
            continue
        v.add(state)
        
        if step > lastStep:
            print(step, len(q))
            lastStep = step
        currentFloor = floorData[floorNum]
        if len(floorData[3]) >= maxItems:
            print("ANS", step)
            return
        
        pairs = set()
        for item in currentFloor:
            isGenerator = item.endswith("G")
            if not isGenerator:
                generator = item + "G"
                if generator in currentFloor:
                    pairs.add(item)
        
        # Try moving down
        if floorNum > 0 and first_nonempty(floorData) < floorNum:
            nextFloor = floorData[floorNum - 1]
            isNextFloorDangerous = is_dangerous(nextFloor)
            
            # What can we move? Try every combination
            for item1, item2 in itt.combinations(currentFloor + [None], 2):
                # If we move this down, is this pair valid?
                nextFloorCopy = nextFloor.copy()
                currentFloorCopy = currentFloor.copy()
                
                if item1 != None:
                    nextFloorCopy.append(item1)
                    currentFloorCopy.remove(item1)
                if item2 != None:
                    nextFloorCopy.append(item2)
                    currentFloorCopy.remove(item2)
                
                # Add state if valid
                if validate_floor(currentFloorCopy) and validate_floor(nextFloorCopy):
                    nextFloorData = floorData.copy()
                    nextFloorData[floorNum] = currentFloorCopy
                    nextFloorData[floorNum - 1] = nextFloorCopy
                    q.append((floorNum - 1, step + 1, nextFloorData))
                
        # Try moving up
        if floorNum < 3:
            nextFloor = floorData[floorNum + 1]
            isNextFloorDangerous = is_dangerous(nextFloor)
            
            # What can we move? Try every combination
            for item1, item2 in itt.combinations(currentFloor + [None], 2):

                
                # If we move this down, is this pair valid?
                nextFloorCopy = nextFloor.copy()
                currentFloorCopy = currentFloor.copy()
                
                if item1 != None:
                    nextFloorCopy.append(item1)
                    currentFloorCopy.remove(item1)
                if item2 != None:
                    nextFloorCopy.append(item2)
                    currentFloorCopy.remove(item2)
                
                # Add state if valid
                if validate_floor(currentFloorCopy) and validate_floor(nextFloorCopy):
                    nextFloorData = floorData.copy()
                    nextFloorData[floorNum] = currentFloorCopy
                    nextFloorData[floorNum + 1] = nextFloorCopy
                    q.append((floorNum + 1, step + 1, nextFloorData))


if __name__ == "__main__":
    main()