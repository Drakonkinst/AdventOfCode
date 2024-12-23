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
    computer_links = {}
    chief_computers = set()
    for line in lines:
        computer_1 = line[:2]
        computer_2 = line[3:]
        if computer_1 not in computer_links:
            computer_links[computer_1] = set()
        if computer_2 not in computer_links:
            computer_links[computer_2] = set()
        computer_links[computer_1].add(computer_2)
        computer_links[computer_2].add(computer_1)
        if computer_1[0] == "t":
            chief_computers.add(computer_1)
        if computer_2[0] == "t":
            chief_computers.add(computer_2)

    q = deque()
    for chief_computer in chief_computers:
        q.append(chief_computer)

    checked_groups = set()
    largest_subset = None
    largest_subset_size = 0
    while q:
        group = q.pop()
        if group in checked_groups:
            continue
        checked_groups.add(group)
        computers = group.split(",")
        if len(computers) > largest_subset_size:
            largest_subset = computers
            largest_subset_size = len(computers)
        leader = computers[0]
        rest = computers[1:]
        overlaps = computer_links[leader]
        for link in rest:
            other_links = computer_links[link]
            overlaps = overlaps.intersection(other_links)
        for overlap in overlaps:
            next_group = computers + [overlap]
            next_group.sort()
            next_key = ",".join(next_group)
            q.append(next_key)

    print(",".join(largest_subset))

def is_connected_to_all(link, rest, computer_links):
    for other in rest:
        other_links = computer_links[other]
        if link not in other_links:
            return False
    return True

if __name__ == "__main__":
    main()