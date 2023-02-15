import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    vowels = set(["a", "e", "i", "o", "u"])
    badPairs = set(["ab", "cd", "pq", "xy"])
    n = 0
    for line in lines:
        numVowels = 0
        lastChar = None
        doubleFound = False
        badPairFound = False
        for i in range(len(line)):
            ch = line[i]
            
            # Check if it is a vowel
            if ch in vowels:
                numVowels += 1
            
            # Check if it is a doubled character
            if lastChar == ch:
                doubleFound = True
            
            # Check if last two characters are a bad pair
            if lastChar != None:
                lastPair = lastChar + ch
                if lastPair in badPairs:
                    badPairFound = True
                    break
            lastChar = ch
        
        # Calculate result
        if doubleFound and numVowels >= 3 and not badPairFound:
            n += 1
    print(n)

if __name__ == "__main__":
    main()