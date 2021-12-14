#!/usr/bin/env python3

# #..#..##...##....##.###..####.#..#..##..
# #..#.#..#.#..#....#.#..#.#....#..#.#..#.
# ####.#....#..#....#.###..###..####.#....
# #..#.#.##.####....#.#..#.#....#..#.#....
# #..#.#..#.#..#.#..#.#..#.#....#..#.#..#.
# #..#..###.#..#..##..###..####.#..#..##..

# H     G    A    J    B    E    H    C

# HGAJBEHC

from operator import itemgetter

def print_board(board):
    res = ""
    for row in board:
        res += "".join(row) + "\n"
        
    print(res)

def count_dots(board):
    result = 0

    for row in board:
        result += row.count("#")

    return result

# ---------------------------------------

def part_one():
    with open("input.txt", "r") as f:
        splitted_f = f.read().split("\n\n")
        str_points = splitted_f[0].split("\n")
        str_folds = splitted_f[1].strip().split("\n")

        # -- parse points
        points = []
        for p in str_points:
            splitted_p = p.split(",")
            x, y = int(splitted_p[0]), int(splitted_p[1])
            points.append((x, y))

        # -- parse folds
        folds = []
        for s_fold in str_folds:
            s_splitted_fold = s_fold.split("fold along ")[1]
            coord, value = s_splitted_fold.split("=")[0], s_splitted_fold.split("=")[1]
            folds.append((coord, int(value)))

        # -- generate board
        x_max = max(points, key=itemgetter(0))[0]
        y_max = max(points, key=itemgetter(1))[1]

        board = [
            ['.' for x in range(0, x_max + 1)]
            for y in range(0, y_max + 1)]

        for (x, y) in points:
            board[y][x] = '#'

        # -- actually do the folds
        for (coord, value) in folds:
            print(count_dots(board))
            rows = len(board)
            columns = len(board[0])
            
            if coord == 'y':
                # -- flip UP with respect to an horizontal line
                new_board = [
                    ['.' for x in range(0, columns)]
                    for y in range(0, value)]

                for y in range(0, len(new_board)):
                    for x in range(0, len(new_board[0])):
                        off = value - y
                        if board[y][x] == '#' or board[value + off][x] == '#':
                            new_board[y][x] = '#'
                        else:
                            new_board[y][x] = '.'
                
            elif coord == 'x':
                # -- flip LEFT with respect to an vertical line
                new_board = [
                    ['.' for x in range(0, value)]
                    for y in range(0, rows)]

                for y in range(0, len(new_board)):
                    for x in range(0, len(new_board[0])):
                        off = value - x
                        if board[y][x] == '#' or board[y][value + off] == '#':
                            new_board[y][x] = '#'
                        else:
                            new_board[y][x] = '.'
                            
            board = new_board
            print_board(board)

        print(count_dots(board))

# ------    

# NOTE: the code for this part two is essentially the same

def part_two():
    with open("input.txt", "r") as f:
        pass

# ------
    
if __name__ == "__main__":
    part_one()
    # part_two()
