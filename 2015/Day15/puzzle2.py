import sys, os, re, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def score(c, ing):
    p = 1
    for i in range(4):
        s = sum([c[j] * ing[j][i] for j in range(len(c))])
        if s <= 0:
            return 0
        p *= s
    return p

def cal(c, ing):
    return sum(c[j] * ing[j][4] for j in range(len(c)))

def main():
    ing = []
    for line in lines:
        w = words(line)
        i = ints(line)
        name = w[0]
        c = i[0]
        d = i[1]
        f = i[2]
        t = i[3]
        l = i[4]
        ing.append([c, d, f, t, l])
        
    total = 100
    print(ing)
    
    maxScore = 0
    maxC = None
    for c in itt.product(*([range(0, total + 1)] * (len(ing) - 1))):
        if sum(c) > total:
            continue
        c = list(c)
        c.append(total - sum(c))
        if cal(c, ing) != 500:
            continue
        s = score(c, ing)
        if s > maxScore:
            maxScore = s
            maxC = c
    print(maxScore, maxC)

if __name__ == "__main__":
    main()