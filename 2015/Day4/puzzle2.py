import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *
import hashlib

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

def main():
    num = 282749  # Start from answer of part 1
    secretKey = lines[0]
    while True:
        # Calculate hash value
        s = secretKey + str(num)
        hashValue = md5(s)
        
        # Check prefix
        hashStart = hashValue[:6]
        if hashStart == "000000":
            print(num)
            return
        num += 1

if __name__ == "__main__":
    main()