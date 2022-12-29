import sys, os, re, itertools
from collections import deque
from sortedcontainers import SortedDict, SortedList
from utils import *

avoid = set([LOWERCASE_STR.index(x) for x in ["i", "o", "l"]])

def incr(s):
    carry = True
    for j in range(len(s) - 1, -1, -1):
        jn = s[j] + 1
        if jn < len(LOWERCASE_STR):
            s[j] = jn
            break
        else:
            s[j] = 0
            if j == 0:
                s.insert(0, 0)
                break
    return s

def fix(s):
    i = 0
    for ch in s:
        if ch in avoid:
            s[i] = ch + 1
            for j in range(i + 1, len(s)):
                s[j] = 0
            return s
        i += 1
    return s

def to_str(s):
    return "".join([LOWERCASE_STR[x] for x in s])

def valid(s):
    a = 0
    b = 0
    lastB = -999
    aDone = False
    lastCh = -999
    
    i = 0
    for ch in s:
        if ch in avoid:
            return False
        if ch == lastCh and i > lastB + 1:
            b += 1
            lastB = i
        if ch == lastCh + 1:
            a += 1
            if a == 2:
                aDone = True
        else:
            a = 0
        lastCh = ch
        i += 1
    return aDone and b >= 2

def main():
    sStr = "cqjxxyzz"
    s = [LOWERCASE_STR.index(ch) for ch in sStr]
    s = incr(s)
    
    while not valid(s):
        #print(to_str(s))
        s = fix(incr(s))
    print(to_str(s))

if __name__ == "__main__":
    main()