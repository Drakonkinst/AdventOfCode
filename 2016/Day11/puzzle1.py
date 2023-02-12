import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def get_pattern(floorNum, generators, chips):
    pairs = []
    for k, v in generators.items():
        pairs.append((v, chips[k]))
    pairs.sort()
    return (floorNum,) + tuple(pairs)

def get_min_floor(generators, chips):
    minValue = 999
    for v in generators.values():
        minValue = min(v, minValue)
    for v in chips.values():
        minValue = min(v, minValue)
    return minValue

def valid_floor(floorNum, generators, chips):
    dangerous = floorNum in generators.values()
    exposed = False
    for k, v in chips.items():
        if v == floorNum and generators[k] != floorNum:
            exposed = True
            break
    valid = not exposed or not dangerous
    return valid

def read_data():
    generators = {}
    chips = {}
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
                generators[element] = i
            elif second.startswith("microchip"):
                nextDash = first.index("-")
                element = first[:nextDash]
                chips[element] = i
            j += 3
    return generators, chips

def get_items_on_floor(lookup, floorNum):
    items = []
    for k, v in lookup.items():
        if v == floorNum:
            items.append(k)
    return items

def print_floors(floorNum, generators, chips):
    generatorsByFloor = [[], [], [], []]
    chipsByFloor = [[], [], [], []]
    
    for k, v in generators.items():
        generatorsByFloor[v].append(k)
    for k, v in chips.items():
        chipsByFloor[v].append(k)
    
    for i in range(3, -1, -1):
        s = ""
        if floorNum == i:
            s += "E"
        else:
            s += " "
        s += "|"
        s += str(generatorsByFloor[i])
        s += "|"
        s += str(chipsByFloor[i])
        print(s)
        
def main():
    generators, chips = read_data()
    maxItems = len(generators) + len(chips)
    print(maxItems)
    
    q = deque([(0, 0, generators, chips)])
    v = set()
    lastStep = -1
    while len(q) > 0:
        step, floorNum, generators, chips = q.popleft()
        pattern = get_pattern(floorNum, generators, chips)
        if pattern in v:
            continue
        v.add(pattern)
        
        generatorsOnThisFloor = [(True, x) for x in get_items_on_floor(generators, floorNum)]
        chipsOnThisFloor = [(False, x) for x in get_items_on_floor(chips, floorNum)]
        toConsider = generatorsOnThisFloor + chipsOnThisFloor + [None]
        minFloor = get_min_floor(generators, chips)
        
        if step > lastStep:
            print("STEP", step, len(q))
            #print_floors(floorNum, generators, chips)
            lastStep = step
        if minFloor == 3:
            print("ANS", step)
            return
        
        # Think about moving down
        if floorNum > get_min_floor(generators, chips):
            for item1, item2 in itt.combinations(toConsider, 2):
                generatorsCopy = generators.copy()
                chipsCopy = chips.copy()
                
                if item1 is not None:
                    if item1[0]:
                        generatorsCopy[item1[1]] -= 1
                    else:
                        chipsCopy[item1[1]] -= 1
                if item2 is not None:
                    if item2[0]:
                        generatorsCopy[item2[1]] -= 1
                    else:
                        chipsCopy[item2[1]] -= 1
                
                if valid_floor(floorNum, generatorsCopy, chipsCopy) and valid_floor(floorNum - 1, generatorsCopy, chipsCopy):
                    q.append((step + 1, floorNum - 1, generatorsCopy, chipsCopy))
    
        # Think about moving up
        if floorNum < 3:
            for item1, item2 in itt.combinations(toConsider, 2):
                generatorsCopy = generators.copy()
                chipsCopy = chips.copy()
                
                if item1 is not None:
                    if item1[0]:
                        generatorsCopy[item1[1]] += 1
                    else:
                        chipsCopy[item1[1]] += 1
                if item2 is not None:
                    if item2[0]:
                        generatorsCopy[item2[1]] += 1
                    else:
                        chipsCopy[item2[1]] += 1
                
                if valid_floor(floorNum, generatorsCopy, chipsCopy) and valid_floor(floorNum + 1, generatorsCopy, chipsCopy):
                    q.append((step + 1, floorNum + 1, generatorsCopy, chipsCopy))
            
    

if __name__ == "__main__":
    main()