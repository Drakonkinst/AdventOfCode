import sys, os, re, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    names = ["children", "cats", "samoyeds", "pomeranians", "akitas", "vizslas", "goldfish", "trees", "cars", "perfumes"]
    values = [3, 7, 2, 3, 0, 0, 5, 3, 2, 1]
    gt = set(["cats", "trees"])
    lt = set(["pomeranians", "goldfish"])
    assert len(names) == len(values)
    
    n = 1
    for line in lines:
        w = words(line)
        i = 2
        good = True
        while i < len(w):
            k = w[i][:-1]
            v = ints(w[i + 1])[0]
            ind = names.index(k)
            
            if k in gt:
                if v <= values[ind]:
                    good = False
                    break
            elif k in lt:
                if v >= values[ind]:
                    good = False
                    break
            else:
                if v != values[ind]:
                    good = False
                    break
            i += 2
        if good:
            print("ANS", n)
            return
        n += 1

if __name__ == "__main__":
    main()