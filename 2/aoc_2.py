#!/usr/bin/env python3


# it seems like the submarine can take a series of commands like
# forward 1, down 2, or up 3:

# - forward X increases the horizontal position by X units.
# - down X increases the depth by X units.
# - up X decreases the depth by X units.

# Calculate the horizontal position and depth you would have after
# following the planned course. What do you get if you multiply your
# final horizontal position by your final depth?

# Result of part one: 1484118
def part_one():
    horizontal_pos = 0
    depth = 0
    
    with open("input.txt", "r") as f:
        for line in f.readlines():

            if line.startswith("forward"):
                horizontal_pos += int(line.split("forward")[1])
            elif line.startswith("down"):
                depth += int(line.split("down")[1])

            elif line.startswith("up"):
                depth -= int(line.split("up")[1])

    print(f"Result of part one: {horizontal_pos * depth}")
    
# -------

# Result of part two: 1463827010
def part_two():
    horizontal_pos = 0
    aim = 0
    depth = 0
    
    with open("input.txt", "r") as f:
        for line in f.readlines():

            if line.startswith("forward"):
                value = int(line.split("forward")[1])
                
                horizontal_pos += value
                depth += aim * value
                
            elif line.startswith("down"):
                aim += int(line.split("down")[1])
            elif line.startswith("up"):
                aim -= int(line.split("up")[1])

    print(f"Result of part two: {horizontal_pos * depth}")

# -------

if __name__ == "__main__":
    part_one()
    part_two()
