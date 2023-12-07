from collections import deque as deq

proggy = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

def addx(x, n, clock):
    return x[-1] + n, clock + 2

def nop(x, clock):
    return x[-1], clock + 1

with open("input10.dat") as inp:
    puzzle = inp.read()

x = [1]
clock = 1
last = None
for instr in puzzle.splitlines():
    opcode = instr.split()[0]
    if opcode == "addx":
        y, clock = addx(x, int(instr.split()[1]), clock)
        x.append(y)
        x.append(y)
        last = addx
    elif opcode == "noop":
        y, clock = nop(x, clock)
        x.append(y)
        last = nop
    else:
        raise ValueError(f"Unknown opcode: {opcode}")
    if (clock % 40 == 20):
        print(f"Signal strength {(clock) * x[-1]} cycle {clock}")
    elif clock % 40 == 21 and last == addx:
        print(f"Signal strength {(clock - 1) * x[-3]} cycle {clock - 1}")
    if clock > 225:
        break

print(sum(x[21:222:40]))
