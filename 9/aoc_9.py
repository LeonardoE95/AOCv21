#!/usr/bin/env python3

# --- Day 9: Smoke Basin ---

# Your first goal is to find the low points - the locations that are
# lower than any of its adjacent locations. Most locations have four
# adjacent locations (up, down, left, and right); locations on the
# edge or corner of the map have three or two adjacent locations,
# respectively. (Diagonal locations do not count as adjacent.)

# The risk level of a low point is 1 plus its height. In the above
# example, the risk levels of the low points are 2, 1, 6, and 6. The
# sum of the risk levels of all low points in the heightmap is
# therefore 15.

# Find all of the low points on your heightmap. What is the sum of the
# risk levels of all low points on your heightmap?

def get_adjacent_positions(lines, max_rows, max_columns, i, j):
    adjacent_positions = []

    # -- corner cases
    if i == 0 and j == 0:
        # -- UP-LEFT corner 
        adjacent_positions = [(0, 1), (1, 0)]

    elif i == max_rows - 1 and j == 0:
        # -- DOWN-LEFT corner
        adjacent_positions = [(max_rows - 2, 0), (max_rows - 1, 1)]

    elif i == 0 and j == max_columns - 1:
        # -- UP-RIGHT corner
        adjacent_positions = [(0, max_columns - 2), (1, max_columns - 1)]

    elif i == max_rows - 1 and j == max_columns - 1:
        # -- UP-DOWN corner
        adjacent_positions = [(max_rows - 1, max_columns - 2), (max_rows - 2, max_columns - 1)]

    # -- edge cases
    elif i == 0:
        adjacent_positions = [(0, j - 1), (0, j + 1), (1, j)]

    elif i == max_rows - 1:
        adjacent_positions = [(max_rows - 1, j - 1), (max_rows - 1, j + 1), (max_rows - 2, j)]
    
    elif j == 0:
        adjacent_positions = [(i - 1, 0), (i + 1, 0), (i, 1)]
    
    elif j == max_columns - 1:
        adjacent_positions = [(i - 1, max_columns - 1), (i + 1, max_columns - 1), (i, max_columns - 2)]

    # -- other cases
    else:
        adjacent_positions = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

    return adjacent_positions

# ---

def low_point(lines, max_rows, max_columns, i, j):
    positions_to_check = get_adjacent_positions(lines, max_rows, max_columns, i, j)
    value = lines[i][j]
    result = True
    for p in positions_to_check:
        i, j = p
        if value >= lines[i][j]:
            result = False
    return result

# ---

def get_low_points(lines):
    max_rows = len(lines)
    max_columns = len(lines[0]) - 1

    points = []
    
    for i in range(0, max_rows):
        for j in range(0, max_columns):
            if low_point(lines, max_rows, max_columns, i, j):
                points.append((i, j))

    return points

# ------------------------------------------------------------

def part_one():
    with open("input.txt", "r") as f:
        lines = f.readlines()

        total_risk_level = 0        
        for p in get_low_points(lines):
            i, j = p
            total_risk_level += 1 + int(lines[i][j])

        print(f"Result of part one {total_risk_level}")

# ------------------------------------------------------------

# Next, you need to find the largest basins so you know what areas are
# most important to avoid.

# A basin is all locations that eventually flow downward to a single
# low point. Therefore, every low point has a basin, although some
# basins are very small.

# NOTE: Locations of height 9 do not count as being in any basin, and
# all other locations will always be part of exactly one basin.

# The size of a basin is the number of locations within the basin,
# including the low point. The example above has four basins.

# Find the three largest basins and multiply their sizes together.

# HOW DO WE FIND A BASIN?

# start with the lower points and expand inversely from those. The
# expansion process looks like this: we get all adjacent points, and
# we filter those based on their value. In particular we only get the
# adjacent points which are +1 the current value we're considering,
# unless that value is '9'. Next we repeat this expansion process
# until there are no more left points. After that we start again with
# the next min point.

def expand_basin(lines, low_p):
    basin = set([low_p])
    points_to_explore = [low_p]

    max_rows = len(lines)
    max_columns = len(lines[0]) - 1

    while len(points_to_explore) > 0:
        p = points_to_explore.pop(0)
        i, j = p
        adjacent_positions = get_adjacent_positions(lines, max_rows, max_columns, i, j)
        
        for adj_p in adjacent_positions:
            i2, j2 = adj_p
            if lines[i2][j2] != '9' and int(lines[i2][j2]) > int(lines[i][j]):
                if adj_p not in basin:
                    basin.add(adj_p)
                    points_to_explore.append(adj_p)

    return basin

# ------

def print_basin(lines, basin):
    print(f"NEW BASIN: {len(basin)}\n")
    for p in basin:
        i, j = p
        print(f"\t {p}, {lines[i][j]}")

# ------

def part_two():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        low_points = get_low_points(lines)

        results = []

        for low_p in low_points:
            basin = expand_basin(lines, low_p)
            basin_size = len(basin)

            print_basin(lines, basin)

            if len(results) < 3:
                results.append(basin_size)
            elif basin_size > min(results):
                results.remove(min(results))
                results.append(basin_size)

        final_res = 1
        for r in results:
            final_res *= r
        print(f"Solution to part two: {final_res}")
            
# ------
    
if __name__ == "__main__":
    part_one()
    part_two()
