#!/usr/bin/env python3

# Bingo is played on a set of boards each consisting of a 5x5 grid of
# numbers. Numbers are chosen at random, and the chosen number is
# marked on all boards on which it appears. (Numbers may not appear on
# all boards.) If all numbers in any row or any column of a board are
# marked, that board wins. (Diagonals don't count.)

# The submarine has a bingo subsystem to help passengers (currently,
# you and the giant squid) pass the time.

# It automatically generates a random order in which to draw numbers
# and a random set of boards (your puzzle input). For example:

# The score of the winning board can now be calculated. Start by
# finding the sum of all unmarked numbers on that board; in this case,
# the sum is 188. Then, multiply that sum by the number that was just
# called when the board won, 24, to get the final score, 188 * 24 =
# 4512.

class Board:
    def __init__(self, board):
        # NOTE: assume board is given as a string
        self.board = board

    def mark(self, n):
        if int(n) < 10:
            self.board = self.board.replace(f" {n} ", " X ")
            self.board = self.board.replace(f" {n}\n", " X\n")
        else:
            self.board = self.board.replace(f"{n}", " X")

    def check_win(self):
        rows = self.board.split("\n")
        for row in rows:
            if row.count("X") == 5:
                return 1
            
        columns = [[rows[j].split()[i] for j in range(0, 5)]
                   for i in range(0, 5)]

        for column in columns:
            if column.count("X") == 5:
                return 1

        return 0

    def compute_score(self, n):
        data = " ".join(self.board.split()).replace("X", "").split()
        res = 0
        for x in data:
            res += int(x)
        return res * int(n)

# ----------------------

def part_one():
    with open("input.txt", "r") as f:
        lines = f.read().split("\n\n")
        number_of_boards = len(lines[1:])
        numbers_drawn = lines[0].split(",")
        boards = [Board(lines[i + 1]) for i in range(0, number_of_boards)]

        for n in numbers_drawn:
            for board in boards:
                board.mark(n)
                if board.check_win():
                    print(f"Result of part one: {board.compute_score(n)}")
                    return

# ------

# Figure out which board will win last. Once it wins, what would its
# final score be?

def part_two():
    with open("input.txt", "r") as f:
        lines = f.read().split("\n\n")        
        numbers_drawn = lines[0].split(",")
        number_of_boards = len(lines[1:])
        boards = [Board(lines[i + 1]) for i in range(0, number_of_boards)]
        boards_finished = set()

        for n in numbers_drawn:
            for j, board in enumerate(boards):
                board.mark(n)
                if board.check_win():
                    if j not in boards_finished:
                        boards_finished.add(j)
                        if len(boards_finished) == number_of_boards:
                            # -- the j-th board is the last one to be filled.f
                            print(f"Result of part two: {board.compute_score(n)}")
                            return                            


# ------

if __name__ == "__main__":
    part_one()
    part_two()
