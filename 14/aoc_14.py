#!/usr/bin/env python3

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

import itertools

def construct_pairs_representation(template, rules):
    unique_letters = "".join(list(set("".join(list(rules.keys())) + "".join(list(rules.values())) + "".join(list(template)))))
    
    # -- initialize pairs representation
    pairs = {}
    for x in itertools.permutations(unique_letters, 2):
        pairs["".join(x)] = 0
    for x in unique_letters:
        pairs[f"{x}{x}"] = 0

    for (x, y) in list(zip(template, template[1:])):
        pairs[f"{x}{y}"] += 1

    return pairs

def even_better_evolve(pairs, rules):
    new_pairs = {x:0 for x in pairs.keys()}
    
    # -- evolve pair representation
    for r in rules:
        if pairs[r] > 0:
            # -- we have a match
            # print(f"Found matching rule: {r} -> {rules[r]}")
            new_pairs[f"{r[0]}{rules[r]}"] += pairs[r]
            new_pairs[f"{rules[r]}{r[1]}"] += pairs[r]

    return new_pairs

def compute_result(template, pairs):
    unique_letters = set("".join(list(pairs.keys())))
    count = {l: 0 for l in unique_letters}
    
    for l in unique_letters:
        for p in pairs:
            if l == f"{p[0]}":
                count[l] += pairs[p]

    # The last letter never changes.
    count[template[-1]] += 1

    sorted_keys = list(count.keys())
    sorted_keys.sort(key=lambda x: count[x], reverse=True)
    
    return count[sorted_keys[0]] - count[sorted_keys[-1]]
                
# ---------------------------------------------

def part_one():
    with open("input.txt", "r") as f:
        s_lines = f.read().split("\n\n")

        # -- read input
        template = s_lines[0].strip()
        
        rules = {}
        for rule in s_lines[1].strip().split("\n"):
            s_rule = rule.split(" -> ")
            rules[s_rule[0]] = s_rule[1]

        pairs = construct_pairs_representation(template, rules)
        for i in range(0, 10):
            pairs = even_better_evolve(pairs, rules)

        result = compute_result(template, pairs)
        print(f"Solution to part one: {result}")
     
# ------
    
def part_two():
    with open("input.txt", "r") as f:
        s_lines = f.read().split("\n\n")

        # -- read input
        template = s_lines[0].strip()
        
        rules = {}
        for rule in s_lines[1].strip().split("\n"):
            s_rule = rule.split(" -> ")
            rules[s_rule[0]] = s_rule[1]

        pairs = construct_pairs_representation(template, rules)
        for i in range(0, 40):
            pairs = even_better_evolve(pairs, rules)

        result = compute_result(template, pairs)
        print(f"Solution to part one: {result}")

# ------
    
if __name__ == "__main__":
    part_one()
    part_two()
