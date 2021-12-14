def get_puzzle(st):
    with open(st, 'r') as file:
        return [line[:-1] for line in file.readlines()]

sample1 = """1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""

class MathLine:
    digits = "0123456789"
    opers = "+*"
    open_ = "("
    close = ")"

    def __init__(self, st):
        self.string = st
        self.value = self.evaluate()

    def evaluate(self):
        stack = []
        output = []
        for tok in self.string[::-1]:
            if tok in MathLine.digits:
                output.append(tok)
            elif tok in MathLine.opers or tok == MathLine.close:
                stack.append(tok)
            elif tok == MathLine.open_:
                while stack[-1] != MathLine.close:
                    output.append(stack.pop())
                stack.pop()
        while stack:
            output.append(stack.pop())
        for tok in output:
            if tok in MathLine.digits:
                stack.append(tok)
            elif tok in MathLine.opers:
                oper1 = stack.pop()
                oper2 = stack.pop()
                if tok == '+':
                    stack.append(str(int(oper1) + int(oper2)))
                elif tok == '*':
                    stack.append(str(int(oper1) * int(oper2)))
        return stack[0]

samples = sample1.split("\n")
results = []
for i, line in enumerate(samples):
    m = MathLine(line)
    results.append(int(m.evaluate()))
    print(f"Evaluation of problem {i} {line} = {m.value}")
print(sum(results))
