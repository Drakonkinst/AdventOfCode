import sys, os, re, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    deer = {}
    for line in lines:
        w = words(line)
        name = w[0]
        speed = int(w[3])
        speedTime = int(w[6])
        restTime = int(w[-2])
        deer[name] = (speed, speedTime, restTime)
    
    n = 2503
    dist = {}
    for k, v in deer.items():
        speed, speedTime, restTime = v
        d = (n // (speedTime + restTime)) * speed * speedTime
        timeLeft = n % (speedTime + restTime)
        speedLeft = min(speedTime, timeLeft)
        d += speed * speedLeft
        dist[k] = d
    print(dist)
    print(max(dist.values()))

if __name__ == "__main__":
    main()