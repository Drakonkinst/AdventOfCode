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
        num_edges = get_num_edges(plots)
        print(region_id, "has", num_edges, "edges and area of", area, "for price of", area * num_edges)
        total += area * num_edges
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
        for offset in CARDINAL_NEIGHBORS:
            neighbor_pos = addT(pos, offset)
            if not in_bounds(neighbor_pos, len(grid), len(grid[0])):
                continue
            neighbor_region_id = grid[neighbor_pos[0]][neighbor_pos[1]]
            if neighbor_region_id == region_id:
                q.append(neighbor_pos)
    regions.append((region_id, plots))

MOVE_DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
LOOK_DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
def get_edge_plots(region):
    edge_plots = set()
    for plot in region:
        for direction in range(len(MOVE_DIRECTIONS)):
            offset = MOVE_DIRECTIONS[direction]
            next_plot = addT(plot, offset)
            if next_plot not in region:
                edge_plots.add((plot, direction))
    print("Found", len(edge_plots), "edge plots")
    return edge_plots

def find_edges(region, starting_plot, starting_direction, plots_to_search):
    print("Starting from", starting_plot, starting_direction)
    plot = starting_plot
    direction = starting_direction
    moving_forward = True
    num_edges = 0
    # Number of edges is equal to the number of direction change
    while not (plot == starting_plot and direction == starting_direction and num_edges > 1):
        move_direction = MOVE_DIRECTIONS[direction]
        look_direction = LOOK_DIRECTIONS[direction]
        print(plot, move_direction, look_direction, moving_forward)
        # Move in direction until you cannot
        if moving_forward:
            move_plot = addT(plot, move_direction)
            if move_plot in region:
                print("Step")
                plot = move_plot
                look_plot = addT(plot, look_direction)
                if look_plot in region:
                    moving_forward = False
            else:
                moving_forward = False
        else:
            num_edges += 1
            look_plot = addT(plot, look_direction)
            if look_plot in region:
                # Concave, turn counterclockwise
                direction = (direction + len(LOOK_DIRECTIONS) - 1) % len(LOOK_DIRECTIONS)
                print("Turn counterclockwise")
            else:
                # Convex, turn clockwise
                direction = (direction + 1) % len(LOOK_DIRECTIONS)
                print("Turn clockwise")
            moving_forward = True
        next_key = (plot, direction)
        if next_key in plots_to_search:
            print("Removing", next_key)
            plots_to_search.remove(next_key)
    return num_edges

def get_num_edges(region):
    plots_to_search = get_edge_plots(region)
    num_edges = 0
    for starting_plot in region:
        for starting_direction in range(len(MOVE_DIRECTIONS)):
            key = (starting_plot, starting_direction)
            if key not in plots_to_search:
                continue
            plots_to_search.remove(key)
            num_edges += find_edges(region, starting_plot, starting_direction, plots_to_search)
    return num_edges
if __name__ == "__main__":
    main()