import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

STRENGTH = "23456789TJQKA"
HAND_LEN = 5

def get_type(hand):
    # [('Q', 3), ('J', 1), ('A', 1)]
    # Then extract values
    most_common = [v for (k, v) in get_most_common(hand)]
    num_unique = len(most_common)
    
    if num_unique == HAND_LEN:
        # High
        return 0
    if num_unique == 4:
        # One pair
        # Pidgeonhole principle
        return 1
    if num_unique == 3 and most_common[0] == 2 and most_common[1] == 2:
        # Two pair
        return 2
    if num_unique == 3 and most_common[0] == 3:
        # Three of a kind
        return 3
    if num_unique == 2 and most_common[0] == 3:
        # Full house
        return 4
    if num_unique == 2 and most_common[0] == 4:
        # Four of a kind
        return 5
    if num_unique == 1:
        return 6
    print("FAIL")
    return -999

def compare_strength(handA, handB):
    for i in range(HAND_LEN):
        valA = STRENGTH.index(handA[i])
        valB = STRENGTH.index(handB[i])
        if valA > valB:
            return 1
        if valB > valA:
            return -1
    return 0
    
def compare(tupleA, tupleB):
    (handA, bidA) = tupleA
    (handB, bidB) = tupleB
    typeA = get_type(handA)
    typeB = get_type(handB)
    if typeA == typeB:
        return compare_strength(handA, handB)
    return typeA - typeB

def main():
    sl = []
    for line in lines:
        w = words(line)
        sl.append((w[0], int(w[1])))
    sort_compare(sl, compare)
    
    total = 0
    for i in range(len(sl)):
        total += (i + 1) * sl[i][1]
    print(total)

if __name__ == "__main__":
    main()