import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

# Didn't manage to get a proper solve for this, so here's my try at a
# slightly better brute-force that searches the inverse maps, starting from 0
# Takes about a minute or so on my machine. Thanks Reddit!
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

def reverse_map(mapArr, val):
    for (destinationStart, sourceStart, rangeLen) in mapArr:
        if destinationStart <= val < destinationStart + rangeLen:
            return sourceStart + (val - destinationStart)
    return val

def reverse_range(maps, val):
    for mapArr in maps:
        val = reverse_map(mapArr, val)
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
    maps.reverse()
    
    # Calculate
    seedRanges = []
    for (seedStart, seedRange) in grouped(seeds, 2):
        seedRanges.append((seedStart, seedStart + seedRange))
    
    locationGuess = 0
    while True:
        seed = reverse_range(maps, locationGuess)
        for (seedStart, seedEnd) in seedRanges:
            if seedStart <= seed < seedEnd:
                print(locationGuess)
                return
        locationGuess += 1

if __name__ == "__main__":
    main()