#!/usr/bin/env python3

from collections import Counter

# --- Day 14: Extended Polymerization ---

# The submarine manual contains instructions for finding the optimal
# polymer formula; specifically, it offers a polymer template and a
# list of pair insertion rules

# The first line is the polymer template - this is the starting point
# of the process.

# The following section defines the pair insertion rules. A rule like
# AB -> C means that when elements A and B are immediately adjacent,
# element C should be inserted between them.

# These insertions all happen simultaneously.

def find_rules(template, rules_prefix):
    """Given a template and a set of rules prefixes, find the ones that
match and return them in a sorted list, where the sorting is done
based on the index of first appearance of the prefix in the template"""

    found_rules = []
    for prefix in rules_prefix:

        # NOTE: be careful of adding all occurences of a given prefix.
        prefix_occ = set()
        occ = template.find(prefix, 0)
        while occ != -1 and occ not in prefix_occ:
            prefix_occ.add(occ)
            occ = template.find(prefix, occ + 1)

        for occ in prefix_occ:
            found_rules.append((prefix, occ))

    found_rules.sort(key=lambda x: x[1])
    return found_rules

def apply_rules(template, rules, found_rules):
    """ Apply given set of rules to given template and return the new template"""
    new_template = ""

    last_index = 0
    for i, rule in enumerate(found_rules):
        prefix, index = rule
        new_template += template[last_index : index + 1] + rules[prefix] + prefix[1]
        last_index = index + 2
    new_template += template[last_index:]
    
    return new_template

def evolve(template, rules):
    """Start from a template and evolve it to the next according to a given set of possible rules"""
    rules_prefix = list(rules.keys())
    found_rules = find_rules(template, rules_prefix)
    new_template = apply_rules(template, rules, found_rules)
    return new_template

def find_most_common(template):
    pass

# --------------------------------------------------------------------

# Apply 10 steps of pair insertion to the polymer template and find
# the most and least common elements in the result. What do you get if
# you take the quantity of the most common element and subtract the
# quantity of the least common element?


def part_one():
    with open("input.txt", "r") as f:
        s_lines = f.read().split("\n\n")

        # -- read input
        template = s_lines[0].strip()
        
        rules = {}
        for rule in s_lines[1].strip().split("\n"):
            s_rule = rule.split(" -> ")
            rules[s_rule[0]] = s_rule[1]
            
        for i in range(0, 40):
            print(f"Starting: {i}...")
            template = evolve(template, rules)
            if i == 25:
                print(template)

        counts = Counter(template)

        sorted_keys = list(counts.keys())
        sorted_keys.sort(key=lambda x : counts[x], reverse=True)

        most_common_key = sorted_keys[0]
        least_common_key = sorted_keys[-1]

        print(f"Result of part one: {counts[most_common_key] - counts[least_common_key]}")

# ------
    
def part_two():
    with open("input.txt", "r") as f:
        pass

# ------
    
if __name__ == "__main__":
    # part_one()
    # part_two()
