import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

# With help from Reddit, since I couldn't figure this one out :(

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

cache = {}
def get_arrangements(record, key):
    k = (record, key)
    if k in cache:
        return cache[k]
    
    # No more keys
    if not key:
        if all(char == "." or char == "?" for char in record):
            cache[k] = 1
            return 1
        cache[k] = 0
        return 0
    
    groupSize = key[0]
    remainingGroups = key[1:]
    minRecordLength = sum(remainingGroups) + len(key) - 1
    count = 0
    
    for i in range(len(record) - minRecordLength - groupSize + 1):
        possibleSubstr = ("." * i) + ("#" * groupSize) + "."
        if all(ch == possibleCh or ch == "?" for (ch, possibleCh) in zip(record, possibleSubstr)):
            count += get_arrangements(record[len(possibleSubstr):], remainingGroups)
    cache[k] = count
    return count

def main():
    total = 0
    for line in lines:
        (record, keyStr) = words(line)
        key = tuple(positive_ints(keyStr))
        count = get_arrangements("?".join([record] * 5), key * 5)
        total += count

    print(total)

if __name__ == "__main__":
    main()