import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

quintuples = {}
triples = deque()
keyIndexes = set()

def check_hash(hashData, index, addTriples):
    lastChar = None
    repeat = 0
    foundTriple = False
    quintuples = set()
    for ch in hashData:
        if ch == lastChar:
            repeat += 1
            if addTriples and repeat >= 3 and not foundTriple:
                triples.append((index, ch))
                foundTriple = True
            if repeat >= 5:
                quintuples.add(ch)
        else:
            repeat = 1
            lastChar = ch
    
    if len(quintuples) > 0:
        i = 0
        while i < len(triples):
            tripleIndex, tripleCh = triples[i]
            if tripleCh in quintuples and tripleIndex < index:
                if tripleIndex not in keyIndexes:
                    print("KEY", tripleIndex, index, tripleCh)
                    keyIndexes.add(tripleIndex)
            i += 1
    
def cull_triples(index):
    while len(triples) > 0 and triples[0][0] < index - 1000:
        triples.popleft()

def main():
    keyNum = 64
    salt = lines[0]
    #salt = "abc"
    index = 0
    while len(keyIndexes) < keyNum:
        data = salt + str(index)
        hashData = md5(data)
        for i in range(2016):
            hashData = md5(hashData)
        cull_triples(index)
        check_hash(hashData, index, True)
        index += 1
    
    # Continue until all triples are resolved
    while len(triples) > 0:
        data = salt + str(index)
        hashData = md5(data)
        for i in range(2016):
            hashData = md5(hashData)
        cull_triples(index)
        # But don't generate new ones
        check_hash(hashData, index, False)
        index += 1
    
    keyIndexesList = list(keyIndexes)
    keyIndexesList.sort()
    print("ANS", keyIndexesList[keyNum - 1])

if __name__ == "__main__":
    main()