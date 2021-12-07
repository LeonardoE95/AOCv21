#!/usr/bin/env python3

# --- Day 7: The Treachery of Whales ---

# You quickly make a list of the horizontal position of each crab
# (your puzzle input). Crab submarines have limited fuel, so you need
# to find a way to make all of their horizontal positions match while
# requiring them to spend as little fuel as possible.

# Each change of 1 step in horizontal position of a single crab costs
# 1 fuel.

# Determine the horizontal position that the crabs can align to using
# the least fuel possible. How much fuel must they spend to align to
# that position?

# Solution: 364898
def part_one():
    with open("input.txt", "r") as f:
        positions = [int(pos) for pos in f.readline().split(",")]
        max_pos = max(positions)
        
        min_fuel = -1
        
        # -- crabs can align in a position within the range [0, max_pos]
        for curr_pos in range(0, max_pos + 1):
            # -- align all crubs to curr_pos and compute fuel used
            fuel_spent = 0
            for pos in positions:
                fuel_spent += abs(pos - curr_pos)

            if min_fuel == -1 or fuel_spent < min_fuel:
                min_fuel = fuel_spent

        print(f"Solution to part one: {min_fuel}")

# ------

# As it turns out, crab submarine engines don't burn fuel at a
# constant rate. Instead, each change of 1 step in horizontal position
# costs 1 more unit of fuel than the last: the first step costs 1, the
# second step costs 2, the third step costs 3, and so on.

# The idea is that now to compute the cost of a movement of n position
# we have to sum the first n numbers with the well known formula

# 1 + 2 + 3 + ... + n = n * (n+1) / 2
    
def part_two():
    with open("input.txt", "r") as f:
        positions = [int(pos) for pos in f.readline().split(",")]
        max_pos = max(positions)
        
        min_fuel = -1
        
        # -- crabs can align in a position within the range [0, max_pos]
        for curr_pos in range(0, max_pos + 1):
            # -- align all crubs to curr_pos and compute fuel used
            fuel_spent = 0
            for pos in positions:
                n = abs(pos - curr_pos)
                fuel_spent += int(n * (n + 1) / 2)

            if min_fuel == -1 or fuel_spent < min_fuel:
                min_fuel = fuel_spent

        print(f"Solution to part one: {min_fuel}")    

# ------
    
if __name__ == "__main__":
    part_one()
    part_two()
