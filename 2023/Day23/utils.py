# Utils inspired by MCPower's utility library
# https://github.com/mcpower/adventofcode/

import re, math, json, hashlib
from functools import cmp_to_key
from collections import Counter

DIGITS = "0123456789"
HEX = "0123456789abcdef"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Directions in clockwise order
CARDINAL_NEIGHBORS = [UP, RIGHT, DOWN, LEFT]
DIAGONAL_NEIGHBORS = [UP, (1, 1), RIGHT, (1, -1), DOWN, (-1, -1), LEFT, (-1, 1)]

# Calls the given function (as a callback) on each element of an iterable
def lmap(func, *iterable):
    return list(map(func, *iterable))

# Creates a 2D array with the given dimensions = (width, height)
# Example: grid = make_grid((100, 100), False)
def make_grid(dimensions, fill=None):
    if len(dimensions) == 1:
        return [fill for _ in range(dimensions[0])]
    next_grid = make_grid(dimensions[1:], fill=fill)
    return [list(next_grid) for _ in range(dimensions[0])]

# Returns a copy of a grid rotated 90 degrees clockwise
def rot_90(l):
    # String version
    # return ["".join(list(reversed(x))) for x in zip(*l)]
    return [list(reversed(x)) for x in zip(*l)]
    
def in_bounds(pos, sizeY, sizeX):
    return 0 <= pos[0] < sizeY and 0 <= pos[1] < sizeX

def find_bounds(arr):
    return min(arr), max(arr)
    
def min_index(arr):
    minIndex = -1
    minValue = math.inf
    for i in range(len(arr)):
        if arr[i] < minValue:
            minValue = arr[i]
            minIndex = i
    return (minIndex, minValue)

def max_index(arr):
    maxIndex = -1
    maxValue = -math.inf
    for i in range(len(arr)):
        if arr[i] > maxValue:
            maxValue = arr[i]
            maxIndex = i
    return (maxIndex, maxValue)

def clamp(value, lo, hi):
    return min(max(value, lo), hi)

def words(s):
    return re.split("\s+", s)

# Methods that extract and collect numbers from a string
def ints(s):
    return lmap(int, re.findall(r"-?\d+", s))
def positive_ints(s):
    return lmap(int, re.findall(r"\d+", s))
def floats(s):
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))
def positive_floats(s):
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))

# Assumes there is a single integer surrounded by non-numeric characters
# More resilient than int()
def parse_int(s):
    return ints(s)[0]

def parse_positive_int(s):
    return positive_ints(s)[0]

# Performs tuple math for a tuple of any length
# Example: addT((0, 1), (1, 0)) -> (1, 1)
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

# Returns JSON object from a string
def parseJSON(j):
    return json.loads(j)

# Returns MD5 hash of a string
def md5(s):
    return hashlib.md5(s.encode()).hexdigest()

# Groups a list into groups of N elements
# Assumes the length of the list is a multiple of N
# grouped([1, 2, 3, 4], 2) -> [(1, 2), (3, 4)]
def grouped(iterable, n):
    return zip(*[iter(iterable)]*n)
    
# Counts a list's elements by frequency using Counter
# returns them sorted as [(item1, frequency1), (item2, frequency2)]
# Works on strings without needing to convert them to a char array
def get_most_common(arr):
    return Counter(arr).most_common()

# Sorts a list using a compare(a, b) function, rather than just getting a value
# Allows for more complex sorting
def sort_compare(arr, compare_func):
    arr.sort(key=cmp_to_key(compare_func))

# To get the bottom N, just invert the value?
class TopN:
    def __init__(self, size, defaultValue = 0, get_value = lambda x : x):
        self.data = [defaultValue for i in range(size)]
        self.get_value = get_value
    
    def add(self, item):
        value = self.get_value(item)
        if value < self.get_value(self.data[-1]):
            return
        i = 0
        insertIndex = -1
        while i < len(self.data):
            if value > self.get_value(self.data[i]):
                insertIndex = i
                break
            i += 1
            
        if insertIndex < 0:
            return

        j = i
        while j < len(self.data) - 1:
            self.data[j + 1] = self.data[j]
            j += 1
        self.data[i] = item
        