import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

TIME_ELAPSED = 100
WIDTH = 101
HEIGHT = 103

def main():
    quadrants = [0, 0, 0, 0]
    for line in lines:
        start_x, start_y, velocity_x, velocity_y = ints(line)
        end_x, end_y = calculate(start_x, start_y, velocity_x, velocity_y)
        quadrant = get_quadrant(end_x, end_y)
        if quadrant > -1:
            quadrants[quadrant] += 1
    print(math.prod(quadrants))

def calculate(start_x, start_y, velocity_x, velocity_y):
    unbounded_x = start_x + velocity_x * TIME_ELAPSED
    unbounded_y = start_y + velocity_y * TIME_ELAPSED
    end_x = unbounded_x % WIDTH
    end_y = unbounded_y % HEIGHT
    if end_x < 0:
        end_x += WIDTH
    if end_y < 0:
        end_y += HEIGHT
    return end_x, end_y

def get_quadrant(end_x, end_y):
    middle_width = WIDTH // 2
    middle_height = HEIGHT // 2
    if end_x == middle_width or end_y == middle_height:
        return -1
    quadrant_x = 0 if end_x < middle_width else 1
    quadrant_y = 0 if end_y < middle_height else 1
    return encode_quadrant(quadrant_x, quadrant_y)

def encode_quadrant(quadrant_x, quadrant_y):
    return quadrant_y * 2 + quadrant_x

if __name__ == "__main__":
    main()