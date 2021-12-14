sample = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

with open("input04.dat") as file:
    lines = file.read()

class BingoBoard:
    def __init__(self, board_lines):
        self.rows = []
        rows = board_lines#.split('\n')
        for row in rows:
            this_row = []
            for n in row.split(' '):
                if n:
                    this_row.append(int(n))
            self.rows.append(this_row)
        self.marks = [5 * [0] for _ in range(5)]
        self.bingo = False

    def next_num(self, num):
        for i, row in enumerate(self.rows):
            for j, val in enumerate(row):
                if val == num:
                    assert(self.marks[i][j] == 0)
                    self.marks[i][j] = 1

    def has_bingo(self):
        for row in self.marks:
            if sum(row) == 5:
                return True
        for i in range(5):
            if sum([row[i] for row in self.marks]) == 5:
                return True
        return False

    def score(self):
        score = 0
        for i, row in enumerate(self.rows):
            for j, val in enumerate(row):
                if not self.marks[i][j]:
                    score += val
        return score

def parse_input(inp):
    lines = inp.split('\n')
    draw_list = [int(x) for x in lines[0].split(',') if x]
    board_list = []
    for i in range(2, len(lines) - 4, 6):
        board_list.append(BingoBoard(lines[i:i+5]))
    return draw_list, board_list


def next_winner(data):
    draw_list, board_list = parse_input(data)
    winners = []
    for num in draw_list:
        for board in [b for b in board_list if not b.bingo]:
            board.next_num(num)
            if board.has_bingo():
                bingo = board.score() * num
                board.bingo = True
                winners.append((board, bingo))
    return winners
            # yield bingo
    # raise StopIteration

def part_one(data):
    return next_winner(data)[0][1]

def part_two(data):
    nw = next_winner(data)
    # while True:
    #     try:
    #         winner = next(nw)
    #     except StopIteration:
    #         return winner
    return nw[-1][1]

print(part_one(lines))
print(part_two(lines))

# import numpy as np
