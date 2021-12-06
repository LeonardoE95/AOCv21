#!/usr/bin/env python3

# --- Day 6: Lanternfish ---

# each lanternfish creates a new lanternfish once every 7 days.

# you can model each fish as a single number that represents the
# number of days until it creates a new lanternfish.

# new lanternfish would surely need slightly longer before it's
# capable of producing more lanternfish: two more days for its first
# cycle.

# Find a way to simulate lanternfish. How many lanternfish would there
# be after 80 days?

def print_population(population):
    keys = list(population.keys())
    keys.sort()

    for k in keys:
        if population[k] > 0:
            print((str(k) + " ") * population[k], end="")
    print()

# ------

def part_one():
    # population[i] := number of lanternfish that will reproduce after i days.
    population = {}
    
    with open("input.txt", "r") as f:
        for n in f.read().split(","):
            population[int(n)] = 1 if int(n) not in population else population[int(n)] + 1

    max_value = max(population.keys())
    for i in range(0, max_value + 1):
        if i not in population:
            population[i] = 0

    # -- now make the population evolve
    days_gone = 0
    while days_gone < 80:        
        # -- number of new lanterfish
        new_lanterfish = population[0]

        # -- scale down the timer of all other lanterfish
        new_population = {}        
        for key in population:
            if key > 0:
                new_population[key - 1] = population[key]

        new_population[0] = 0 if 0 not in new_population else new_population[0]
        new_population[6] = new_lanterfish if 6 not in new_population else new_population[6] + new_lanterfish
        new_population[8] = new_lanterfish if 8 not in new_population else new_population[8] + new_lanterfish
        
        population = new_population        
        days_gone += 1

    print(f"Result of part one: {sum(population.values())}")

# ------

def part_two():
    # population[i] := number of lanternfish that will reproduce after i days.
    population = {}
    
    with open("input.txt", "r") as f:
        for n in f.read().split(","):
            population[int(n)] = 1 if int(n) not in population else population[int(n)] + 1

    max_value = max(population.keys())
    for i in range(0, max_value + 1):
        if i not in population:
            population[i] = 0

    # -- now make the population evolve
    days_gone = 0
    while days_gone < 256:        
        # -- number of new lanterfish
        new_lanterfish = population[0]

        # -- scale down the timer of all other lanterfish
        new_population = {}        
        for key in population:
            if key > 0:
                new_population[key - 1] = population[key]

        new_population[0] = 0 if 0 not in new_population else new_population[0]
        new_population[6] = new_lanterfish if 6 not in new_population else new_population[6] + new_lanterfish
        new_population[8] = new_lanterfish if 8 not in new_population else new_population[8] + new_lanterfish
        
        population = new_population        
        days_gone += 1

    print(f"Result of part two: {sum(population.values())}")

# ------
    
if __name__ == "__main__":
    part_one()
    part_two()
