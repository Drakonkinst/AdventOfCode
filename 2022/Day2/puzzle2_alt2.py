import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

abc = "ABC"
xyz = "XYZ"

def get_you(enemy, outcome):
    if outcome == 0:
        return (enemy + 3 - 1) % 3
    if outcome == 1:
        return enemy
    return (enemy + 1) % 3
        
def main():
    total = 0
    for line in lines:
        w = words(line)
        enemy = abc.index(w[0])
        outcome = xyz.index(w[1])
        you = get_you(enemy, outcome)
        total += outcome * 3
        total += you + 1
    print(total)

if __name__ == "__main__":
    main()