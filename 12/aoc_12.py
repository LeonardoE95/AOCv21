#!/usr/bin/env python3

# --- Day 12: Passage Pathing ---

# So, all paths you find should visit small caves at most once, and
# can visit big caves any number of times.

# How many paths through this cave system are there that visit small
# caves at most once?

def count_paths_part_1(graph, current_node, visited_small_caves):
    # -- base cases
    if current_node == 'end':
        return 1
    if current_node not in graph:
        return 0
    else:
        result = 0
        updated_visited_small_caves = visited_small_caves.copy()
        
        # -- visit current_node
        if current_node.islower():
            updated_visited_small_caves.add(current_node)

        # -- recurse on all of its neighbours
        for possible_node in graph[current_node]:
            # -- we can only go once for each lower-node
            if possible_node.islower() and possible_node not in updated_visited_small_caves:
                result += count_paths_part_1(graph, possible_node, updated_visited_small_caves)
            elif possible_node.isupper():
                result += count_paths_part_1(graph, possible_node, updated_visited_small_caves)

        return result

def create_graph(lines):
    # NOTE: the graph is bi-directional    
    graph = {}

    for line in lines:
        splitted_l = line.split("-")
        node1, node2 = splitted_l[0].strip(), splitted_l[1].strip()

        # add edge 'node1 -> node2'
        if node1 not in graph:
            graph[node1] = [node2]
        else:
            graph[node1].append(node2)

        # add edge 'node2 -> node1'
        if node2 not in graph:
            graph[node2] = [node1]
        else:
            graph[node2].append(node1)        

    return graph
    
    
# -----------------------------------
    
def part_one():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        # -- build graph structure by reading input
        graph = create_graph(lines)
        # -- visit the graph and count the paths
        result = count_paths_part_1(graph, "start", set())
        print(f"Result of part one: {result}")

# ---------------------------

# In the path now we can choose a single small cave to be visited more
# than once, but only a single for the entire run.

def count_paths_part_2(graph, current_node, visited_small_caves, small_cave, small_cave_count):
    # -- base cases
    if current_node == 'end':
        return int(small_cave_count == 0)
    elif current_node not in graph:
        return 0
    else:
        result = 0
        updated_visited_small_caves = visited_small_caves.copy()
        
        # -- visit current_node
        if current_node.islower():
            updated_visited_small_caves.add(current_node)

        # -- visit all of its neighbours
        for possible_node in graph[current_node]:
            if possible_node.islower():
                if possible_node == small_cave and small_cave_count > 0:
                    result += count_paths_part_2(graph, possible_node, updated_visited_small_caves, small_cave, small_cave_count - 1)
                elif possible_node not in updated_visited_small_caves:
                    result += count_paths_part_2(graph, possible_node, updated_visited_small_caves, small_cave, small_cave_count)
            elif possible_node.isupper():
                result += count_paths_part_2(graph, possible_node, updated_visited_small_caves, small_cave, small_cave_count)
        return result
    
def part_two():
    graph = {}
    with open("input.txt", "r") as f:
        lines = f.readlines()

        # -- build graph structure by reading input
        graph = create_graph(lines)

        # -- visit the graph and count the paths
        final_res = 0        
        small_caves = [n for n in graph if n.islower() and n != 'start' and n != 'end']
        for cave in small_caves:
            final_res += count_paths_part_2(graph, "start", set(), cave, 2)
        final_res += count_paths_part_1(graph, "start", set())
        
        print(f"Result of part two: {final_res}")
        
# ------
    
if __name__ == "__main__":
    part_one()
    part_two()
