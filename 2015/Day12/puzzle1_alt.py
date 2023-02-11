import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

# The funny solution
def main():
    print(sum(ints(lines[0])))
    
if __name__ == "__main__":
    main()