import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

abc = "ABC"
xyz = "XYZ"

def get_score(enemy, you):
    if enemy == you:
        # Tie
        return 3
    if (you + 1) % 3 == enemy:
        # Lose
        return 0
    # Win
    return 6
        
def main():
    total = 0
    for line in lines:
        w = words(line)
        enemy = abc.index(w[0])
        you = xyz.index(w[1])
        total += get_score(enemy, you)
        total += you + 1
    print(total)

if __name__ == "__main__":
    main()