import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    numElves = int(lines[0])
    elves = [i + 1 for i in range(numElves)]
    
    # Loop until there are only 2 Elves left
    while len(elves) > 2:
        newElves = []
        
        # If there are an odd number of Elves
        # The last Elf steals the first
        if len(elves) % 2 == 0:
            i = 0
        else:
            i = 2
        
        # Every other Elf steals successfully
        while i < len(elves):
            newElves.append(elves[i])
            i += 2
        elves = newElves
    
    # If there are only 2 Elves, the first one always wins
    # If there is only 1 Elf, they win
    print(elves[0])
    

if __name__ == "__main__":
    main()