#!/usr/bin/env python3

import math
import heapq

# You start in the top left position, your destination is the bottom
# right position, and you cannot move diagonally.
#
# The number at each position is its risk level; to determine the
# total risk of an entire path, add up the risk levels of each
# position you enter.
#
# Your goal is to find a path with the lowest total risk. In this
# example, a path with the lowest total risk is highlighted here:

def get_adjacent(max_rows, max_cols, x, y):
    possible_pos = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
    return [(x, y) for (x, y) in possible_pos if x >=0 and x < max_rows and y >= 0 and y < max_cols]

def dijkstra(positions, grid, s):
    distance = {}
    found_pos_opt = {}
    heap = []

    n_rows = len(grid)
    n_cols = len(grid[0])

    for p in positions:
        distance[p] = math.inf if p != s else 0
        found_pos_opt[p] = False

    s_x, s_y = s
    heapq.heappush(heap, (distance[s], s))

    while heap:
        _, u = heapq.heappop(heap)

        if found_pos_opt[u]:
            continue

        # used to not having to implement decrease-key operation
        found_pos_opt[u] = True

        u_x, u_y = u
        for v in get_adjacent(n_rows, n_cols, u_x, u_y):
            v_x, v_y = v

            if distance[v] == math.inf:
                distance[v] = distance[u] + grid[v_x][v_y]
                heapq.heappush(heap, (distance[v], v))
                
            elif distance[u] + grid[v_x][v_y] < distance[v]:
                distance[v] = distance[u] + grid[v_x][v_y]
                heapq.heappush(heap, (distance[v], v))
                        
    return distance

# ----------------------------------------------
    
def part_one():
    with open("input.txt", "r") as f:
        grid = []

        for line in f.readlines():
            rows = [int(n) for n in list(line) if n != '\n']
            grid.append(rows)

        n_rows = len(grid)
        n_cols = len(grid[0])

        s = (0, 0)
        positions = []
        for x in range(0, n_rows):
            for y in range(0, n_cols):
                positions.append((x, y))
        
        distances = dijkstra(positions, grid, (0, 0))
        result = distances[(n_rows - 1, n_cols - 1)]
        
        print(f"Solution to part one: {result}")
        
# ----------------------------------------------

def grow_horizontally(grid, level):
    new_grid = []
    
    for old_row in grid:
        new_row = []
        for i in range(1, level + 1):
            new_row += [x + i if x + i <= 9 else ((x + i) % 9) for x in old_row]
        new_grid.append(old_row + new_row)

    return new_grid
        
def grow_vertically(grid, level):
    new_grid = grid.copy()

    for i in range(1, level + 1):
        for old_row in grid:
            new_row = [x + i if x + i <= 9 else ((x + i) % 9) for x in old_row]
            new_grid.append(new_row)

    return new_grid

def part_two():
    with open("input.txt", "r") as f:
        grid = []

        for line in f.readlines():
            rows = [int(n) for n in list(line) if n != '\n']
            grid.append(rows)

        # first, grow horizontally
        grid = grow_horizontally(grid, 4)
        # then, vertically
        grid = grow_vertically(grid, 4)

        # finally, compute shortest paths like before
        n_rows = len(grid)
        n_cols = len(grid[0])

        s = (0, 0)
        positions = []
        for x in range(0, n_rows):
            for y in range(0, n_cols):
                positions.append((x, y))
        
        distances = dijkstra(positions, grid, (0, 0))
        result = distances[(n_rows - 1, n_cols - 1)]
        
        print(f"Solution to part two: {result}")        

# ------
    
if __name__ == "__main__":
    part_one()
    part_two()
