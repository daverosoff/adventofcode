sample="""#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""

class Claim:
    def __init__(self, line):
        prefix, suffix = line.split(' @ ')
        self.id = int(prefix[1:])
        coords, dims = suffix.split(': ')
        self.y, self.x = [int(t) for t in coords.split(',')]
        self.dy, self.dx = [int(t) for t in dims.split('x')]

        # self.dx -= 1
        # self.dy -= 1


claims = [Claim("#0 @ 0,0: 0x0")]
# for line in sample.split('\n'):
    # claims.append(Claim(line))

with open('input03.dat', 'r') as file:
    for line in file.readlines():
        claims.append(Claim(line))

claim_nums = [c.id for c in claims] []

xmax = max([c.x + c.dx for c in claims])
ymax = max([c.y + c.dy for c in claims])
board = [['.'] * (ymax + 1) for _ in range(xmax + 1)]

print(len(claim_nums))
for i, c in enumerate(claims):
    for x in range(c.x, c.x + c.dx):
        for y in range(c.y, c.y + c.dy):
            if board[x][y] == '.':
                board[x][y] = '1'
            elif board[x][y] == '1':
                board[x][y] = 'X'
                if c.id in claim_nums:
                    claim_nums.remove(c.id)
            elif board[x][y] == 'X':
                pass
            else:
                raise IndexError('wtf')

flat = [ch for row in board for ch in row]
# for row in board:
    # print(" ".join(row))
print(flat.count('X'))
# print([(i, j) for i, x in enumerate(board) for j, y in enumerate(x) if y == '1'])
print(len(claim_nums))