#!/usr/bin/env python3

# count the number of times a depth measurement increases from the
# previous measurement. (There is no measurement before the first
# measurement.) In the example above, the changes are as follows:

# 199 (N/A - no previous measurement)
# 200 (increased)
# 208 (increased)
# 210 (increased)
# 200 (decreased)
# 207 (increased)
# 240 (increased)
# 269 (increased)
# 260 (decreased)
# 263 (increased)

def part_one():
    tot = 0
    with open("input.txt") as f:
        lines = f.readlines()
        last_val = int(lines[0])
        
        for line in lines[1:]:
            curr_val = int(line)

            if last_val < curr_val:
                tot += 1

            last_val = curr_val
            
    print(f"Result of part one: {tot}")

# -----

# consider sums of a three-measurement sliding window. Again
# considering the above example

# 199  A      
# 200  A B    
# 208  A B C  
# 210    B C D
# 200  E   C D
# 207  E F   D
# 240  E F G  
# 269    F G H
# 260      G H
# 263        H

# count the number of times the sum of measurements in this sliding
# window increases from the previous sum.

def part_two():
    tot = 0
    with open("input.txt") as f:
        lines = f.readlines()
        length = len(lines)
        i = 0
        
        last_val = -1
        if length > 3:
            last_val = int(lines[0]) + int(lines[1]) + int(lines[2])
            i += 3
        else:
            return

        for i in range(1, length):
            curr_val = -1

            if i + 2 < length:
                curr_val = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
                i += 3
            else:
                break

            if last_val < curr_val:
                tot += 1

            last_val = curr_val
            
    print(f"Result of part one: {tot}")
    
if __name__ == "__main__":
    part_one()
    part_two()
