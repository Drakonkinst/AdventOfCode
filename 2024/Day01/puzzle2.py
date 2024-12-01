import sys, os, itertools as itt
from collections import deque # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    left = []
    right = []
    for line in lines:
        vals = ints(line)
        left.append(vals[0])
        right.append(vals[1])
    frequency = Counter(right)
    similarity_score = 0
    for num in left:
        num_appearances = frequency[num]
        score = num * num_appearances
        similarity_score += score
    print(similarity_score)

if __name__ == "__main__":
    main()