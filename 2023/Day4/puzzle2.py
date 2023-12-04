import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    cards = []
    for line in lines:
        w = words(line)
        separatorIndex = w.index("|")
        winningNums = ints(" ".join(w[2:separatorIndex]))
        myNums = ints(" ".join(w[separatorIndex + 1:]))
        cards.append((winningNums, myNums))
        
    q = deque()
    for i in range(len(cards)):
        q.append(i + 1)
    total += len(cards)
    results = {}
    while q:
        nextCardNum = q.popleft()
        if not (nextCardNum - 1 < len(cards)):
            continue
        
        numWins = 0
        if nextCardNum in results:
            numWins = results[nextCardNum]
        else:
            (winningNums, myNums) = cards[nextCardNum - 1]
            for myNum in myNums:
                if myNum in winningNums:
                    numWins += 1
        if numWins > 0:
            for i in range(numWins):
                total += 1
                q.append(nextCardNum + i + 1)
        results[nextCardNum] = numWins
    print(total)

if __name__ == "__main__":
    main()