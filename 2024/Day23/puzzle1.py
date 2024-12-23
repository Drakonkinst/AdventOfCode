import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    total = 0
    computers = {}
    chief_computers = set()
    for line in lines:
        computer_1 = line[:2]
        computer_2 = line[3:]
        if computer_1 not in computers:
            computers[computer_1] = set()
        if computer_2 not in computers:
            computers[computer_2] = set()
        computers[computer_1].add(computer_2)
        computers[computer_2].add(computer_1)
        if computer_1[0] == "t":
            chief_computers.add(computer_1)
        if computer_2[0] == "t":
            chief_computers.add(computer_2)

    q = deque()
    for chief_computer in chief_computers:
        links = computers[chief_computer]
        for link in links:
            q.append(sort_pair(link, chief_computer))

    checked_pairs = set()
    sets_of_3 = set()
    while q:
        pair = q.pop()
        if pair in checked_pairs:
            continue
        checked_pairs.add(pair)
        computer_1, computer_2 = pair
        links_1 = computers[computer_1]
        links_2 = computers[computer_2]
        overlaps = links_1.intersection(links_2)
        for overlap in overlaps:
            sets_of_3.add(sort_trio(computer_1, computer_2, overlap))
    print(len(sets_of_3))

def sort_pair(computer_1, computer_2):
    if computer_1 < computer_2:
        return (computer_1, computer_2)
    return (computer_2, computer_1)

def sort_trio(computer_1, computer_2, computer_3):
    arr = [computer_1, computer_2, computer_3]
    arr.sort()
    return tuple(arr)

if __name__ == "__main__":
    main()