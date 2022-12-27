# Utils inspired by MCPower's utility library
# https://github.com/mcpower/adventofcode/

import re

def lmap(func, *iterables):
    return list(map(func, *iterables))

def make_grid(*dimensions, fill=None):
    if len(dimensions) == 1:
        return [fill for _ in range(dimensions[0])]
    next_grid = make_grid(*dimensions[1:], fill=fill)
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
