import sys, os, re, math, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

r = 3010
c = 3019

def main():
    
    # Find the point along the first column that this diagonal is a part of
    # by decrementing column and incrementing row until column is 1
    # Then add the column value which is now the offset along the diagonal
    # of the index to calculate
    # Find the sum with the triangle numbers formula
    n = (r + c - 1) * (r + c - 2) // 2 + c
    print("n", n)
    
    # Calculate value
    v = 20151125
    for i in range(n - 1):
        v = (v * 252533) % 33554393
    print("v", v)


if __name__ == "__main__":
    main()