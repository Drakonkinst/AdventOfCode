import sys, os, re, itertools as itt
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    deer = {}
    scores = {}
    dist = {}
    for line in lines:
        w = words(line)
        name = w[0]
        speed = int(w[3])
        speedTime = int(w[6])
        restTime = int(w[-2])

        deer[name] = (speed, speedTime, restTime)
        scores[name] = 0
        dist[name] = 0
    
    n = 2503
    winningDist = -1
    for i in range(n):
        for k, v in deer.items():
            speed, speedTime, restTime = v
            cycle = i % (speedTime + restTime)
            if cycle < speedTime:
                dist[k] += speed
                if dist[k] > winningDist:
                    winningDist = dist[k]
        for k in deer.keys():
            if dist[k] == winningDist:
                scores[k] += 1
    print(scores)
    print(max(scores.values()))

if __name__ == "__main__":
    main()