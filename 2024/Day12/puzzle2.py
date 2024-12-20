import sys, os, itertools as itt
from collections import deque, Counter # append(), pop(), popleft()
from queue import PriorityQueue # put(), get()
from sortedcontainers import SortedDict, SortedList
from utils import *
from functools import cache
sys.setrecursionlimit(10000)

file = open("input.txt", "r")
lines = [line.strip() for line in file.readlines()]

MOVE_DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
LOOK_DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def main():
    regions = []
    visited = set()
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            pos = (row, col)
            if pos in visited:
                continue
            calculate_region(lines, pos, regions, visited)
    total = 0
    for region in regions:
        region_id, plots = region
        area = len(plots)
        edges = gather_edge_cells(plots)
        num_sides = get_num_sides(edges, plots)
        total += area * num_sides
    print(total)

def calculate_region(grid, start_pos, regions, visited):
    region_id = grid[start_pos[0]][start_pos[1]]
    q = deque()
    q.append(start_pos)
    plots = []
    while len(q):
        pos = q.pop()
        if pos in visited:
            continue
        visited.add(pos)
        plots.append(pos)
        for index in range(len(LOOK_DIRECTIONS)):
            offset = LOOK_DIRECTIONS[index]
            neighbor_pos = addT(pos, offset)
            if not in_bounds(neighbor_pos, len(grid), len(grid[0])):
                continue
            neighbor_region_id = grid[neighbor_pos[0]][neighbor_pos[1]]
            if neighbor_region_id == region_id:
                q.append(neighbor_pos)
    regions.append((region_id, plots))

def gather_edge_cells(region):
    edges = set()
    for plot in region:
        for index in range(len(LOOK_DIRECTIONS)):
            offset = LOOK_DIRECTIONS[index]
            next_plot = addT(plot, offset)
            if next_plot not in region:
                edges.add((plot, index))
    return edges

def find_edges(plots, starting_plot, starting_direction, visited_plots):
    plot = starting_plot
    direction = starting_direction
    moving_forward = True
    num_edges = 0
    # Number of edges is equal to the number of direction change
    while not (plot == starting_plot and direction == starting_direction and num_edges > 1):
        move_direction = MOVE_DIRECTIONS[direction]
        look_direction = LOOK_DIRECTIONS[direction]
        # Move in direction until you cannot
        if moving_forward:
            move_plot = addT(plot, move_direction)
            if move_plot in plots:
                plot = move_plot
                look_plot = addT(plot, look_direction)
                if look_plot in plots:
                    moving_forward = False
            else:
                moving_forward = False
        else:
            num_edges += 1
            look_plot = addT(plot, look_direction)
            if look_plot in plots:
                # Concave, turn counterclockwise
                direction = (direction + len(LOOK_DIRECTIONS) - 1) % len(LOOK_DIRECTIONS)
            else:
                # Convex, turn clockwise
                direction = (direction + 1) % len(LOOK_DIRECTIONS)
            moving_forward = True
        next_key = (plot, direction)
        visited_plots.add(next_key)
    return num_edges

def get_num_sides(edges, plots):
    visited_edges = set()
    total = 0
    for edge in edges:
        if edge in visited_edges:
            continue
        starting_plot, starting_direction = edge
        total += find_edges(plots, starting_plot, starting_direction, visited_edges)
    return total

if __name__ == "__main__":
    main()