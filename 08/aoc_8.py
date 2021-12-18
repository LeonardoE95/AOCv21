#!/usr/bin/env python3

"""

digit 0 uses 6 segments
digit 1 uses 2 segments
digit 2 uses 5 segments
digit 3 uses 5 segments
digit 4 uses 4 segments
digit 5 uses 5 segments
digit 6 uses 6 segments
digit 7 uses 3 segments
digit 8 uses 7 segments
digit 9 uses 6 segments
"""

import itertools

# how many times do digits 1, 4, 7, or 8 appear?
def part_one():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        digits = [0 for i in range(0, 10)]
        
        for line in lines:
            output_values = line.split("|")[1].split()

            for val in output_values:
                if len(val) == 2:
                    digits[1] += 1
                elif len(val) == 4:
                    digits[4] += 1
                elif len(val) == 3:
                    digits[7] += 1
                elif len(val) == 7:
                    digits[8] += 1

        print(f"Solution to part one: {sum(digits)}")

# ------    

# For each entry, determine all of the wire/segment connections and
# decode the four-digit output values. What do you get if you add up
# all of the output values?

SEGM2DIG = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9'
}

# def decode_mappings(input_values):
#     # Initially this is unknown
#     seg2wire = {
#         'a': set(),
#         'b': set(),
#         'c': set(),
#         'd': set(),
#         'e': set(),
#         'f': set(),
#         'g': set(),
#     }
    
#     wire_1 = ""
#     wire_4 = ""
#     wire_7 = ""
#     wire_8 = ""
    
#     # --------------------------------
#     # -- get wires of well known digit
#     for val in input_values:
#         if len(val) == 2:
#             wire_1 = set(list(val))
#         elif len(val) == 3:
#             wire_7 = set(list(val))
#         elif len(val) == 4:
#             wire_4 = set(list(val))
#         elif len(val) == 7:
#             wire_8 = set(list(val))

#     # --------------------------------
#     # -- figure out which wire gets mapped to segment A
#     seg2wire['a'] = wire_7 - wire_1

#     # --------------------------------
#     # -- figure out which wire gets mapped to segment C
#     tmp = ""
#     for val in input_values:
#         if len(val) == 6:
#             tmp += "".join(set(wire_8) - set(list(val)))
#     seg2wire['c'] = wire_1.intersection(set(list(tmp)))

#     # --------------------------------
#     # -- figure out which wire gets mapped to segment F
#     seg2wire['f'] = wire_7 - seg2wire['c'] - seg2wire['a']

#     # --------------------------------
#     # -- figure out which wire gets mapped to segment D
#     known_values = set(list(seg2wire['a']) + list(seg2wire['c']) + list(seg2wire['f']))
#     tmp = []
#     for val in input_values:
#         set_val = set(list(val))
#         if len(set_val - known_values) == 2:
#             for x in (set_val - known_values):
#                 if x not in tmp:
#                     tmp.append(x)
#                 else:
#                     seg2wire['d'] = set(x)

#     # --------------------------------
#     # -- figure out which wire gets mapped to segment B
#     seg2wire['b'] = wire_4 - set(list(seg2wire['c']) + list(seg2wire['d']) + list(seg2wire['f']))

#     # --------------------------------
#     # -- figure out which wire gets mapped to segment G
#     known_values = set(list(seg2wire['a']) + list(seg2wire['c']) + list(seg2wire['d']) + list(seg2wire['f']))
#     for val in input_values:
#         set_val = set(list(val)) - known_values
#         if len(set_val) == 1 and list(set_val)[0] != list(seg2wire['b'])[0]:
#             seg2wire['g'] = set_val

#     # --------------------------------
#     # -- figure out which wire gets mapped to segment E
#     known_values = set([list(x)[0] for x in seg2wire.values() if len(x) > 0])
#     seg2wire['e'] = set(seg2wire.keys()) - known_values

#     result = [list(x)[0] for x in seg2wire.values()]
#     return result

def wire2seg(value, connections):
    """This function takes a value of wires which are turned on and a set
    of connection between wires and segments and returns the value of
    the segments which are turned on.
    
    The value returned can be used to understand which digit is shown
    with the given wires.

    The connections are given with a list, where the index of the list
    represents a wire, and the value of the list represents a
    segment. For example the list

    ['d', 'g', 'b', 'c', 'a', 'e', 'f']

    represents that the following situation:

    - The wire 'a' is used to turn on the segment 'd'
    - The wire 'b' is used to turn on the segment 'g'
    - The wire 'c' is used to turn on the segment 'b'
    - The wire 'd' is used to turn on the segment 'c'
    - The wire 'e' is used to turn on the segment 'a'
    - The wire 'f' is used to turn on the segment 'e'
    - The wire 'g' is used to turn on the segment 'f'

    Thus, the sequence of wires 'cfbegad' is mapped to the sequence of
    segments 'begafdc', which represents the digit '8'.

    """

    seg_str = ""

    for c in list(value):
        # go from the wire value to the segment value
        seg_str += chr(ord('a') + connections.index(c))

    return "".join(sorted(seg_str))


def decode_mappings(input_values):
    values = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    
    for perm in itertools.permutations(values):
        # check if using the given permutation is we're able to cover
        # all of the digits with the given input vales.
        
        found_digits = {
            'abcefg': False,   # 0
            'cf': False,       # 1
            'acdeg': False,    # 2
            'acdfg': False,    # 3
            'bcdf': False,     # 4
            'abdfg': False,    # 5
            'abdefg': False,   # 6
            'acf': False,      # 7
            'abcdefg': False,  # 8
            'abcdfg': False    # 9
        }
        
        for wire_str in input_values:
            segment_str = wire2seg(wire_str, perm)

            if segment_str not in found_digits:
                # -- this perm is not valid
                break
            else:
                found_digits[segment_str] = True

        if sum(list(found_digits.values())) == 10:
            return perm

def part_two():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        final_result = 0        
        for line in lines:
            input_values = line.split("|")[0].split()
            output_values = line.split("|")[1].split()
            mappings = decode_mappings(input_values)
            
            line_res = ''
            for wire_str in output_values:
                segment_str = wire2seg(wire_str, mappings)
                line_res += SEGM2DIG[segment_str]

            final_result += int(line_res)

        print(f"Solution to part two: {final_result}")
                
# ------
    
if __name__ == "__main__":
    part_one()
    part_two()
