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
    for line in lines:
        num = ints(line)[0]
        total += generate(num)
    print(total)

def generate(secret):
    for _ in range(2000):
        secret = next_secret(secret)
    return secret

def next_secret(secret):
    secret = mix(secret, secret << 6)
    secret = prune(secret)
    secret = mix(secret, secret >> 5)
    secret = prune(secret)
    secret = mix(secret, secret << 11)
    secret = prune(secret)
    return secret

def mix(a, b):
    return a ^ b

def prune(a):
    return a % 16777216


if __name__ == "__main__":
    main()