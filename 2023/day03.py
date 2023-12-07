import numpy as np

sample2 = """12.......*..
+.........34
.......-12..
..78........
..*....60...
78.........9
.5.....23..$
8...90*12...
............
2.2......12.
.*.........*
1.1..503+.56"""

sample = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def parse(puzz: str) -> list[list[str]]:
    rows = puzz.split('\n')
    result = []
    for row in rows:
        if row:
            result.append([ch for ch in row])
    return result

def is_symbol(ch: str) -> bool:
    return not ch == "." and not ch.isnumeric()

def numeric_vectors(puzz: list[list[str]]) -> list[list[bool]]:
    return [[ch.isnumeric() for ch in row] for row in puzz]

def is_touching(puzz: list[list[str]], x: int, y: int, xmax: int, ymax: int) -> bool:
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == dy == 0:
                continue
            if (0 <= x + dx < xmax) and (0 <= y + dy < ymax):
                if is_symbol(puzz[x + dx][y + dy]):
                    return True
    return False

class StateMachine:
    def __init__(self, puzz: str):
        self.puzz = parse(puzz)
        self.x, self.y = 0, 0
        self.state = 'q1'
        self.xmax = len(self.puzz)
        self.ymax = len(self.puzz[0])
        self.stack = []
        self.partnos = []

    def next_move(self):
        match self.state:
            case 'q1': self.do_q1()
            case 'q2': self.do_q2()
            case 'q3': self.do_q3()
            case 'q4': self.do_q4()

    def advance_pos(self):
        self.y += 1
        if self.y >= self.ymax:
            self.x += 1
            self.y = 0

    def do_q1(self):
        current = self.puzz[self.x][self.y]
        match current:
            case '-':
                next_state = 'q4'
                touching = is_touching(self.puzz, self.x, self.y, self.xmax, self.ymax)
                self.stack.append((current, touching))
            case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9': # found a number
                next_state = 'q2'
                touching = is_touching(self.puzz, self.x, self.y, self.xmax, self.ymax)
                self.stack.append((current, touching))
            case _:
                next_state = 'q1'
        self.advance_pos()
        if self.x >= self.xmax:
            next_state = 'q3'
        self.state = next_state

    def do_q2(self):
        current = self.puzz[self.x][self.y]
        match current:
            case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9': # found a number
                next_state = 'q2'
                touching = is_touching(self.puzz, self.x, self.y, self.xmax, self.ymax)
                self.stack.append((current, touching))
            case _:
                next_state = 'q1'
                is_part_number = False
                part_number = 0
                i = 0
                while self.stack:
                    digit, touch = self.stack.pop()
                    match digit:
                        case '-':
                            part_number *= -1
                        case _:
                            part_number += int(digit) * 10 ** i
                    is_part_number |= touch
                    i += 1
                if is_part_number:
                     self.partnos.append(part_number)
        self.advance_pos()
        if self.x >= self.xmax:
            next_state = 'q3'
        self.state = next_state

    def do_q3(self):
        print(sum(self.partnos))
        self.state = 'done'

    def do_q4(self):
        current = self.puzz[self.x][self.y]
        match current:
            case '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9': # found a number
                next_state = 'q2'
                touching = is_touching(self.puzz, self.x, self.y, self.xmax, self.ymax)
                self.stack.append((current, touching))
            case _:
                next_state = 'q1'
                while self.stack:
                    self.stack.pop()
        self.advance_pos()
        if self.x >= self.xmax:
            next_state = 'q3'
        self.state = next_state

# print(read_number(parse(sample), 0, 0))
sm = StateMachine(sample2)
while sm.state != 'done':
    sm.next_move()
with open('input03.dat', 'r') as f:
    puzz01 = StateMachine(f.read())
while puzz01.state != 'done':
    puzz01.next_move()