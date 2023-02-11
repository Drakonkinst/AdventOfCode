import sys, os, re, math, itertools as itt
from collections import deque, Counter
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    result = ""
    l = len(lines[0])
    
    data = []
    for i in range(l):
        data.append([])

    for line in lines:
        for i in range(len(line)):
            data[i].append(line[i])
    
    for i in range(l):
        mostCommon = Counter(data[i]).most_common()[-1][0]
        result += mostCommon
    print(result)

if __name__ == "__main__":
    main()