import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    results = {}
    for line in lines:
        w = words(line)
        separatorIndex = w.index("|")
        cardNum = ints(w[1])[0]
        winningNums = lmap(int, w[2:separatorIndex])
        myNums = lmap(int, w[separatorIndex + 1:])
        
        numWins = 0
        for myNum in myNums:
            if myNum in winningNums:
                numWins += 1
        results[cardNum] = numWins
    
    q = deque()
    for i in range(len(lines)):
        q.append(i + 1)
    while q:
        cardNum = q.popleft()
        total += 1
        for i in range(results[cardNum]):
            q.append(cardNum + i + 1)
    print(total)

if __name__ == "__main__":
    main()