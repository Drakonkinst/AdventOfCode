import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def next_block(startIndex, ignoreFirst = True):
    index = startIndex
    linesInBlock = []
    first = True
    while index < len(lines):
        line = lines[index]
        if line:
            if first and ignoreFirst:
                first = False
                index += 1
                continue
            linesInBlock.append(line)
        else:
            break
        index += 1
    return (index + 1, to_grid(linesInBlock))

def to_grid(lines):
    return [ints(line) for line in lines]

def do_map(mapArr, val):
    for (destinationStart, sourceStart, rangeLen) in mapArr:
        if sourceStart <= val < sourceStart + rangeLen:
            #print(destinationStart, sourceStart, rangeLen)
            return destinationStart + (val - sourceStart)
    return val

def do_range(maps, val):
    for mapArr in maps:
        val = do_map(mapArr, val)
    return val

def main():
    # Parse
    index = 0
    (index, seeds) = next_block(index, False)
    seeds = seeds[0]
    (index, seedToSoil) = next_block(index)
    (index, soilToFertilizer) = next_block(index)
    (index, fertilizerToWater) = next_block(index)
    (index, waterToLight) = next_block(index)
    (index, lightToTemperature) = next_block(index)
    (index, temperatureToHumidity) = next_block(index)
    (index, humidityToLocation) = next_block(index)
    
    maps = [seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation]
    
    # Calculate
    minLocation = math.inf
    for seed in seeds:
        location = do_range(maps, seed)
        minLocation = min(location, minLocation)
    print(minLocation)

if __name__ == "__main__":
    main()