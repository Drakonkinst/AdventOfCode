# Utils inspired by MCPower's utility library
# https://github.com/mcpower/adventofcode/

import re, json, hashlib

HEX_STR = "0123456789abcdef"
LOWERCASE_STR = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_STR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

CARDINAL_NEIGHBORS = [UP, RIGHT, DOWN, LEFT]
DIAGONAL_NEIGHBORS = [UP, (1, 1), RIGHT, (1, -1), DOWN, (-1, -1), LEFT, (-1, 1)]

def lmap(func, *iterables):
    return list(map(func, *iterables))

def make_grid(dimensions, fill=None):
    if len(dimensions) == 1:
        return [fill for _ in range(dimensions[0])]
    next_grid = make_grid(dimensions[1:], fill=fill)
    return [list(next_grid) for _ in range(dimensions[0])]

def find_bounds(arr):
    return min(arr), max(arr)

def clamp(value, lo, hi):
    return min(max(value, lo), hi)

def ints(s):
    return lmap(int, re.findall(r"-?\d+", s))
def positive_ints(s):
    return lmap(int, re.findall(r"\d+", s))
def floats(s):
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))
def positive_floats(s):
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))
def words(s):
    return s.split(' ')
    
def addT(tuple1, tuple2):
    return tuple([tup[0] + tup[1] for tup in zip(tuple1, tuple2)])
def subT(tuple1, tuple2):
    return tuple([tup[0] - tup[1] for tup in zip(tuple1, tuple2)])
def multT(tuple1, tuple2):
    return tuple([tup[0] * tup[1] for tup in zip(tuple1, tuple2)])
def divT(tuple1, tuple2):
    return tuple([tup[0] / tup[1] for tup in zip(tuple1, tuple2)])

def arrow(ch):
    if ch == '<':
        return LEFT
    elif ch == '>':
        return RIGHT
    elif ch == 'v':
        return DOWN
    elif ch == '^':
        return UP
    return (0, 0)

def parseJSON(j):
    return json.loads(j)
    
def md5(s):
    return hashlib.md5(s.encode()).hexdigest()