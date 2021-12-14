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

# --------------------------------------------------------------------

def part_one():
    with open("tmp.txt", "r") as f:
        s_lines = f.read().split("\n\n")

        # -- read input
        template = s_lines[0].strip()
        
        rules = {}
        for rule in s_lines[1].strip().split("\n"):
            s_rule = rule.split(" -> ")
            rules[s_rule[0]] = s_rule[1]
        rules_prefix = list(rules.keys())

        # print(found_rules)
        # _, min_index = found_rules[0]
        # _, max_index = found_rules[len(found_rules) - 1]

        template = "NBCCNBBBCBHCB"
        
        found_rules = []
        for prefix in rules_prefix:
            prefix_index = template.find(prefix)
            if prefix_index != -1:
                found_rules.append((prefix, prefix_index))

        found_rules.sort(key=lambda x: x[1])

        print(found_rules)


        # j = 0
        # while j < 4:

        #     found_rules = []
        #     for prefix in rules_prefix:
        #         prefix_index = template.find(prefix)
        #         if prefix_index != -1:
        #             found_rules.append((prefix, prefix_index))

        #     found_rules.sort(key=lambda x: x[1])
            
        #     final_template = ""
        #     last_index = 0
        #     for i, rule in enumerate(found_rules):
        #         prefix, index = rule
        #         final_template += template[last_index : index + 1] + rules[prefix] + prefix[1]
        #         last_index = index + 2
        #     final_template += template[last_index: ]

        #     template = final_template

        #     print(final_template)
        #     j += 1

         
        
        # new_template = template
        # for i, r in enumerate(found_rules):
        #     prefix, index = r
        #     print(f"Before applying rule {prefix, index}")
        #     print(f"\t{new_template}")
        #     print(rules[prefix])
        #     new_template = new_template[:index + i] + rules[prefix] + template[index + 1 + i:]

        # print(new_template)

        # -- iterate process as long as some rules can be used.
        # done = False
        # while not done:
        #     matching_rules = []
        #     pass



# ------
    
def part_two():
    with open("input.txt", "r") as f:
        pass

# ------
    
if __name__ == "__main__":
    part_one()
    # part_two()
