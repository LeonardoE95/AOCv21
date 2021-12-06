#!/usr/bin/env python3

# --- Day 5: Hydrothermal Venture ---
# https://adventofcode.com/2021/day/5

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def generate_points(p1, p2):
    # generate all points between p1 and p2
    if p1.x == p2.x:
        # -- vertical line
        if p1.y < p2.y:
            return [Point(p1.x, y) for y in range(p1.y, p2.y + 1)]
        else:
            return [Point(p1.x, y) for y in range(p2.y, p1.y + 1)]
            
    elif p1.y == p2.y:
        # -- horizontal line
        if p1.x < p2.x:
            return [Point(x, p1.y) for x in range(p1.x, p2.x + 1)]
        else:
            return [Point(x, p1.y) for x in range(p2.x, p1.x + 1)]

    else:
        # -- diagonal line
        if p1.x < p2.x and p1.y < p2.y:
            return [Point(p1.x + i, p1.y + i) for i in range(0, p2.x - p1.x + 1)]
        elif p1.x < p2.x and p1.y > p2.y:
            return [Point(p1.x + i, p1.y - i) for i in range(0, p2.x - p1.x + 1)]
        elif p1.x > p2.x and p1.y < p2.y:
            return [Point(p1.x - i, p1.y + i) for i in range(0, p2.y - p1.y + 1)]
        elif p1.x > p2.x and p1.y > p2.y:
            return [Point(p1.x - i, p1.y - i) for i in range(0, p1.y - p2.y + 1)]

def compute_score(points):
    count_points = {}
    for p in points:
        count_points[str(p)] = 1 if str(p) not in count_points else count_points[str(p)] + 1

    # print(count_points)

    result = 0
    for v in count_points.values():
        if v >= 2:
            result += 1

    return result

# --------

def part_one():
    max_point = 9
    points = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            p1, p2 = line.split("->")[0], line.split("->")[1]
            
            p1 = Point(int(p1.split(",")[0]), int(p1.split(",")[1]))
            p2 = Point(int(p2.split(",")[0]), int(p2.split(",")[1]))

            if (p1.x == p2.x) or (p1.y == p2.y):
                for p in generate_points(p1, p2):
                    points.append(p)

        # -- now we can count how many points are on the same square.
        print(f"Result of part one: {compute_score(points)}")
            
# ------    
    
def part_two():
    max_point = 9
    points = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            p1, p2 = line.split("->")[0], line.split("->")[1]
            
            p1 = Point(int(p1.split(",")[0]), int(p1.split(",")[1]))
            p2 = Point(int(p2.split(",")[0]), int(p2.split(",")[1]))

            for p in generate_points(p1, p2):
                points.append(p)
            
        # -- now we can count how many points are on the same square.
        print(f"Result of part two: {compute_score(points)}")
    
# ------
    
if __name__ == "__main__":
    # part_one()
    part_two()    

