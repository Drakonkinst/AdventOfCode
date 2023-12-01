import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

wordDigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def main():
    total = 0
    for line in lines:
        firstDigit = None
        firstIndex = len(lines)
        lastDigit = None
        lastIndex = -1
        
        for d in DIGITS:
            digit = str(d)
            if digit in line:
                startIndex = line.index(digit)
                endIndex = line.rindex(digit)
                if startIndex < firstIndex:
                    firstIndex = startIndex
                    firstDigit = digit
                if endIndex > lastIndex:
                    lastIndex = endIndex
                    lastDigit = digit
        
        for d in wordDigits:
            digit = str(wordDigits.index(d) + 1)
            if d in line:
                startIndex = line.index(d)
                endIndex = line.rindex(d)
                if startIndex < firstIndex:
                    firstIndex = startIndex
                    firstDigit = digit
                if endIndex > lastIndex:
                    lastIndex = endIndex
                    lastDigit = digit 
        
        total += int(firstDigit + lastDigit)
    print(total)

if __name__ == "__main__":
    main()