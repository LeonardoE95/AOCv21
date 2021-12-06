#!/usr/bin/env python3

# --- Day 3: Binary Diagnostic ---
# https://adventofcode.com/2021/day/3

def compute_ones_dict(lines):
    # returns a list ones such that
    # 
    # ones[i] := number of 1s in i-th column with respect to binary
    # numbers in lines.
    
    ones = {}
    bit_length = len(lines[0]) - 1  # NOTE: removing '\n'
    
    for line in lines:
        for i in range(0, bit_length):
            if i not in ones:
                # -- init-case
                ones[i] = 0 if line[i] == '0' else 1
            elif line[i] == '1':
                ones[i] += 1
                
    return ones

def compute_ones_by_column(lines, i):
    # returns a number which represents the number of 1s in the i-th
    # column of the given input lines.
    ones = 0

    for line in lines:
        if line[i] == '1':
            ones += 1

    return ones

# --------------

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
        bit_length = len(lines[0]) - 1  # NOTE: removing '\n'
        
        ones = compute_ones_dict(lines)

        for i in range(0, bit_length):
            if ones[i] > int(tot_lines / 2):
                # there are more 1s than 0s in the i-th column
                gamma_rate += '1'
                epsilon_rate += '0'
            else:
                # there are more 0s than 1s in the i-th column
                gamma_rate += '0'
                epsilon_rate += '1'

    print(f"Result of part one: {int(gamma_rate, 2) * int(epsilon_rate, 2)}")
                
# ----------------------------------

def filter_bits(lines, j, criteria):
    # -- base case
    if len(lines) == 1:
        return int(lines[0], 2)
    else:
        new_lines = []
        ones = compute_ones_by_column(lines, j)
        zeroes = len(lines) - ones

        for number in lines:
            
            if criteria == 'oxygen':
                if ones > zeroes and number[j] == '1':
                    new_lines.append(number)
                elif ones < zeroes and number[j] == '0':
                    new_lines.append(number)
                elif ones == zeroes and number[j] == '1':
                    new_lines.append(number)
                    
            elif criteria == 'co2-scrubber':
                if ones > zeroes and number[j] == '0':
                    new_lines.append(number)
                elif ones < zeroes and number[j] == '1':
                    new_lines.append(number)
                elif ones == zeroes and number[j] == '0':
                    new_lines.append(number)

        return filter_bits(new_lines, j + 1, criteria)

# SOLUTION: Result of part two: 4375225
def part_two():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        oxygen_rating = filter_bits(lines, 0, 'oxygen')
        co2_rating = filter_bits(lines, 0, 'co2-scrubber')
        print(f"Result of part two: {oxygen_rating * co2_rating}")
      
# # ----------------------------------

if __name__ == "__main__":
    part_one()
    part_two()
