import sys, os, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

STRENGTH = "J23456789TQKA"
HAND_LEN = 5
JOKER = "J"

def get_type(hand):
    counts = Counter([ch for ch in hand])
    most_common = counts.most_common()
    # [('Q', 3), ('J', 1), ('A', 1)]
    
    if JOKER in hand:
        max_type = 0
        for ch in STRENGTH:
            if ch == JOKER:
                continue
            max_type = max(max_type, get_type(hand.replace(JOKER, ch)))
        return max_type
    else:
        if len(most_common) == HAND_LEN:
            # High
            return 0
        if len(most_common) == 4:
            # One pair
            # Pidgeonhole principle
            return 1
        if len(most_common) == 3 and most_common[0][1] == 2 and most_common[1][1] == 2:
            # Two pair
            return 2
        if len(most_common) == 3 and most_common[0][1] == 3:
            # Three of a kind
            return 3
        if len(most_common) == 2 and most_common[0][1] == 3:
            # Full house
            return 4
        if len(most_common) == 2 and most_common[0][1] == 4:
            # Four of a kind
            return 5
        if len(most_common) == 1:
            return 6
    print("UNKNOWN")
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
    sl.sort(key=cmp_to_key(compare))
    
    total = 0
    for i in range(len(sl)):
        total += (i + 1) * sl[i][1]
    print(total)

if __name__ == "__main__":
    main()