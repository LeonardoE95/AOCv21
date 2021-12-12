#!/usr/bin/env python3

# --- Day 11: Dumbo Octopus ---

def get_adjacent(n_rows, n_columns, x, y):
    possible_pos = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
                    (x + 1, y + 1), (x + 1, y - 1),
                    (x - 1, y + 1), (x - 1, y - 1)]

    return [(x, y) for (x, y)
            in possible_pos if x >= 0 and x < n_rows and y >= 0 and y < n_columns]

def print_grid(grid):
    n_rows = len(grid)
    n_columns = len(grid[0])

    s = ""
    for x in range(0, n_rows):
        for y in range(0, n_columns):
            s += str(grid[x][y])
        s += "\n"

    print(s)

# ---------------------------

def part_one():
    grid = []
    steps_left = 100
    total_flashes = 0
    
    with open("input.txt", "r") as f:
        for line in f.readlines():
            row = [int(c) for c in line if c != '\n']
            grid.append(row)

        n_rows = len(grid)
        n_columns = len(grid[0])

        while steps_left > 0:

            # -- increase level of each octopus
            for x in range(0, n_rows):
                for y in range(0, n_columns):
                    grid[x][y] += 1
                    
            # -- keep flashing octopus with energy level > 9
            done = False
            flashing_octopuses = set()
            while not done:
                done = True
                for x in range(0, n_rows):
                    for y in range(0, n_columns):
                        if grid[x][y] > 9 and (x, y) not in flashing_octopuses:
                            # -- flash this
                            for (p_x, p_y) in get_adjacent(n_rows, n_columns, x, y):
                                grid[p_x][p_y] += 1

                            # -- update count
                            flashing_octopuses.add((x, y))
                            total_flashes += 1
                            done = False

            for (p_x, p_y) in flashing_octopuses:
                grid[p_x][p_y] = 0

            # print(f"After step: {max_steps - steps_left + 1}")
            # print_grid(grid)
            # print("====")
                
            # -- decrease count for next iteration
            steps_left -= 1

        print(f"Result of part one: {total_flashes}")
        
# ---------------------------
    
def part_two():
    grid = []
    result = -1
    
    with open("input.txt", "r") as f:
        for line in f.readlines():
            row = [int(c) for c in line if c != '\n']
            grid.append(row)

        n_rows = len(grid)
        n_columns = len(grid[0])

        steps_done = 1
        while result == -1:
            # -- increase level of each octopus
            for x in range(0, n_rows):
                for y in range(0, n_columns):
                    grid[x][y] += 1
                    
            # -- keep flashing octopus with energy level > 9
            done = False
            flashing_octopuses = set()
            while not done:
                done = True
                for x in range(0, n_rows):
                    for y in range(0, n_columns):
                        if grid[x][y] > 9 and (x, y) not in flashing_octopuses:
                            # -- flash this
                            for (p_x, p_y) in get_adjacent(n_rows, n_columns, x, y):
                                grid[p_x][p_y] += 1

                            # -- update count
                            flashing_octopuses.add((x, y))
                            done = False

            for (p_x, p_y) in flashing_octopuses:
                grid[p_x][p_y] = 0


            # all octopuses flashed
            if len(flashing_octopuses) == (n_rows * n_columns):
                result = steps_done
                break

            # print(f"After step: {max_steps - steps_left + 1}")
            # print_grid(grid)
            # print("====")
                
            # -- decrease count for next iteration
            steps_done += 1

        print(f"Result of part two: {result}")    

# ------
    
if __name__ == "__main__":
    # part_one()
    part_two()
