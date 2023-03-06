import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    for line in lines:
        wordList = words(line)
        encounteredWords = set()
        valid = True
        for word in wordList:
            letters = [ch for ch in word]
            letters.sort()
            sortedWord = "".join(letters)
            if sortedWord in encounteredWords:
                valid = False
                break
            encounteredWords.add(sortedWord)
        if valid:
            total += 1
    print(total)

if __name__ == "__main__":
    main()