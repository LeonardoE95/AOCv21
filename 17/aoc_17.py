#!/usr/bin/env python3

# --- Day 17: Trick Shot ---

# The probe's x,y position starts at 0,0. Then, it will follow some
# trajectory by moving in steps. On each step, these changes occur in
# the following order:
#
# - The probe's x position increases by its x velocity.
#
# - The probe's y position increases by its y velocity.
#
# - Due to drag, the probe's x velocity changes by 1 toward the value
#   0; that is, it decreases by 1 if it is greater than 0, increases
#   by 1 if it is less than 0, or does not change if it is already 0.
#
#
# - Due to gravity, the probe's y velocity decreases by 1.
#
# For the probe to successfully make it into the trench, the probe
# must be on some trajectory that causes it to be within a target area
# after any step.
#
# Find the initial velocity that causes the probe to reach the highest
# y position and still eventually be within the target area after any
# step. What is the highest y position it reaches on this trajectory?

def part_one():
    with open("tmp.txt", "r") as f:
        line = f.read().split()
        x_coords = line[2].split("=")[1][:-1].split("..")
        y_coords = line[3].split("=")[1].split("..")
        
        print(x_coords)
        print(y_coords)        

# ----------
    
def part_two():
    with open("input.txt", "r") as f:
        pass

# ----------
    
if __name__ == "__main__":
    part_one()
    # part_two()
