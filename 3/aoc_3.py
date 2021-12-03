#!/usr/bin/env python3

# --- Day 3: Binary Diagnostic ---
# https://adventofcode.com/2021/day/3

# The submarine has been making some odd creaking noises, so you ask
# it to produce a diagnostic report just in case.

# The diagnostic report (your puzzle input) consists of a list of
# binary numbers which, when decoded properly, can tell you many
# useful things about the conditions of the submarine. The first
# parameter to check is the power consumption.

# You need to use the binary numbers in the diagnostic report to
# generate two new binary numbers (called the gamma rate and the
# epsilon rate). The power consumption can then be found by
# multiplying the gamma rate by the epsilon rate.

# Each bit in the gamma rate can be determined by finding the most
# common bit in the corresponding position of all numbers in the
# diagnostic report.

# The epsilon rate is calculated in a similar way; rather than use the
# most common bit, the least common bit from each position is used. So,
# the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate
# (22) by the epsilon rate (9) produces the power consumption, 198.

# For example,

# 00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010

# we get

# gamma rate   --> 10110 = 22
# epsilon rate --> 01001 = 9

# SOLUTION: Result of part one: 3885894
def part_one():
    gamma_rate = ""
    epsilon_rate = ""

    # ones[i] := number of 1s in i-th column with respect to all
    # binary numbers.
    ones = {}
    
    with open("input.txt", "r") as f:
        lines = f.readlines()
        tot_lines = len(lines)
        bit_length = len(lines[0]) - 1 # NOTE: removing '\n'
        
        # -- initialization
        for i in range(0, bit_length):
            if lines[0][i] == '1':
                ones[i] = 1
            else:
                ones[i] = 0
            
        # -- rest of stuff
        for line in lines[1:]:
            for i in range(0, bit_length):
                if line[i] == '1':
                    ones[i] += 1

        # -- now I can get compute both gamma and epsilon
        for i in range(0, bit_length):

            if ones[i] > int(tot_lines / 2):
                # there are more 1s than 0s for the i-th column
                gamma_rate += '1'
                epsilon_rate += '0'
            else:
                gamma_rate += '0'
                epsilon_rate += '1'

    print(f"Result of part one: {int(gamma_rate, 2) * int(epsilon_rate, 2)}")
                
# ----------------------------------

# Both the oxygen generator rating and the CO2 scrubber rating are
# values that can be found in your diagnostic report. Both values are
# located using a similar process that involves filtering out values
# until only one remains.

# Before searching for either rating value, start with the full list
# of binary numbers from your diagnostic report and consider just the
# first bit of those numbers. Then:

# - Keep only numbers selected by the bit criteria for the type of
#   rating value for which you are searching. Discard numbers which do
#   not match the bit criteria.

# - If you only have one number left, stop; this is the rating value
#   for which you are searching.

# - Otherwise, repeat the process, considering the next bit to the
#   right.

# The bit criteria depends on which type of rating value you want to find:

# To find oxygen generator rating, determine the most common value (0
# or 1) in the current bit position, and keep only numbers with that
# bit in that position. If 0 and 1 are equally common, keep values
# with a 1 in the position being considered.

# To find CO2 scrubber rating, determine the least common value (0 or
# 1) in the current bit position, and keep only numbers with that bit
# in that position. If 0 and 1 are equally common, keep values with a
# 0 in the position being considered.

def compute_ones(lines, i):
    ones = 0

    for line in lines:
        if line[i] == '1':
            ones += 1

    return ones

# SOLUTION: Result of part two: 4375225
def part_two():
    oxygen_rating = -1
    co2_rating = -1
    
    with open("input.txt", "r") as f:
        lines = f.readlines()
        bit_length = len(lines[0]) - 1 # NOTE: removing '\n'
        last_tmp_numbers_2 = lines     # this for CO2 scrubber rating

        # this for oxygen generator rating
        last_tmp_numbers = lines    
        for i in range(0, bit_length):
            new_tmp_numbers = []
            
            length = len(last_tmp_numbers)
            ones = compute_ones(last_tmp_numbers, i)
            zeroes = length - ones
            
            for number in last_tmp_numbers:
                if ones > zeroes and number[i] == '1':
                    new_tmp_numbers.append(number)
                elif ones < zeroes and number[i] == '0':
                    new_tmp_numbers.append(number)
                elif ones == zeroes and number[i] == '1':
                    new_tmp_numbers.append(number)
                    
            # -- this for oxygen generator rating
            if len(new_tmp_numbers) == 1:
                oxygen_rating = int(new_tmp_numbers[0], 2)
                break

            last_tmp_numbers = new_tmp_numbers

        # --------------------------------
        # this for CO2 scrubber rating
        last_tmp_numbers = lines    
        for i in range(0, bit_length):
            new_tmp_numbers = []
            
            length = len(last_tmp_numbers)
            ones = compute_ones(last_tmp_numbers, i)
            zeroes = length - ones
            
            for number in last_tmp_numbers:
                if ones > zeroes and number[i] == '0':
                    new_tmp_numbers.append(number)
                elif ones < zeroes and number[i] == '1':
                    new_tmp_numbers.append(number)
                elif ones == zeroes and number[i] == '0':
                    new_tmp_numbers.append(number)
                    
            # -- this for oxygen generator rating
            if len(new_tmp_numbers) == 1:
                co2_rating = int(new_tmp_numbers[0], 2)
                break

            last_tmp_numbers = new_tmp_numbers

        print(f"Result of part two: {oxygen_rating * co2_rating}")
      
# ----------------------------------

if __name__ == "__main__":
    part_one()
    part_two()
