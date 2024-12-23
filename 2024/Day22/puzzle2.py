import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

N = 4
def main():
    all_sequences = {}
    for line in lines:
        num = ints(line)[0]
        generate(num, all_sequences)
    highest_key, highest_value = get_highest_entry(all_sequences)
    print(highest_value)

def generate(secret, all_sequences):
    last_n_price_changes = deque()
    last_price = get_price(secret)
    visited = set()
    for _ in range(2000):
        secret = next_secret(secret)
        price = get_price(secret)
        price_change = price - last_price
        last_n_price_changes.append(price_change)
        # Should only need to do it once
        if len(last_n_price_changes) > N:
            last_n_price_changes.popleft()
        if len(last_n_price_changes) == N:
            key = get_key(last_n_price_changes)
            if key not in visited:
                visited.add(key)
                if key not in all_sequences:
                    all_sequences[key] = 0
                all_sequences[key] += price
        last_price = price
        # print(format(secret, '#026b'))

def get_key(last_n_prices):
    s = ""
    for i in range(N):
        s += str(last_n_prices[i])
        if i < N - 1:
            s += ","
    return s

def get_highest_entry(dictionary):
    highest_value = 0
    highest_key = None
    for k, v in dictionary.items():
        if v > highest_value:
            highest_value = v
            highest_key = k
    return highest_key, highest_value

def next_secret(secret):
    secret = mix(secret, secret << 6)
    secret = prune(secret)
    secret = mix(secret, secret >> 5)
    secret = prune(secret)
    secret = mix(secret, secret << 11)
    secret = prune(secret)
    return secret

def get_price(secret):
    return secret % 10

def mix(a, b):
    return a ^ b

def prune(a):
    return a % 16777216

if __name__ == "__main__":
    main()